package com.example.demo.config;

import com.datastax.oss.driver.api.core.CqlSession;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class CassandraConnectionCheck implements CommandLineRunner {

    private static final Logger logger = LoggerFactory.getLogger(CassandraConnectionCheck.class);

    @Value("${spring.data.cassandra.contact-points}")
    private String cassandraHost;

    @Value("${spring.data.cassandra.port}")
    private int cassandraPort;

    private final CqlSession cqlSession;

    public CassandraConnectionCheck(CqlSession cqlSession) {
        this.cqlSession = cqlSession;
    }

    @Override
    public void run(String... args) {
        logger.info("🔵 Making connection to Cassandra at {}:{}.", cassandraHost, cassandraPort);

        if (!cqlSession.getMetadata().getNodes().isEmpty()) {
            logger.info("🟢 Connected to Cassandra at {}:{}.", cassandraHost, cassandraPort);
        } else {
            logger.error("🔴 Failed to connect to Cassandra at {}:{}.", cassandraHost, cassandraPort);
        }
    }

    // @Override
    // public void run(String... args) throws InterruptedException {
    //     final int maxAttempts = 5;
    //     int attempt = 1;

    //     while (attempt <= maxAttempts) {
    //         try {
    //             logger.info("Attempt {}: Making connection to Cassandra at {}:{}", attempt, cassandraHost, cassandraPort);
    //             if (!cqlSession.getMetadata().getNodes().isEmpty()) {
    //                 logger.info("Connected to Cassandra at {}:{}", cassandraHost, cassandraPort);
    //                 break; // Successful connection, exit the loop
    //             } else {
    //                 logger.error("Failed to connect to Cassandra at {}:{}", cassandraHost, cassandraPort);
    //             }
    //         } catch (Exception e) {
    //             logger.error("Attempt {}: Error connecting to Cassandra: {}", attempt, e.getMessage());
    //         }

    //         if (attempt < maxAttempts) {
    //             logger.info("Waiting for 10 seconds before retrying...");
    //             Thread.sleep(10000); // Wait for 10 seconds
    //         }
    //         attempt++;
    //     }

    //     if (attempt > maxAttempts) {
    //         logger.error("Failed to connect to Cassandra after {} attempts", maxAttempts);
    //     }
    // }
}
