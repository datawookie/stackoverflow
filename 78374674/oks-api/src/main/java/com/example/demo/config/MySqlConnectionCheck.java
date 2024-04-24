package com.example.demo.config;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Component;

import javax.sql.DataSource;
import java.sql.Connection;

@Component
public class MySqlConnectionCheck implements CommandLineRunner {

    private static final Logger logger = LoggerFactory.getLogger(MySqlConnectionCheck.class);

    // Inject database properties from application.properties
    @Value("${spring.datasource.url}")
    private String dbUrl;

    @Value("${spring.datasource.username}")
    private String username;

    @Value("${spring.datasource.password}")
    private String password;

    private final DataSource dataSource;

    public MySqlConnectionCheck(DataSource dataSource) {
        this.dataSource = dataSource;
    }

    @Override
    public void run(String... args) {
        logger.info(" Making connection to MySQL database.");

        try (Connection connection = dataSource.getConnection()) {
            // You can execute a simple query here to test the connection
            String query = "SELECT 1";
            int result = connection.createStatement().executeQuery(query).getInt(1);

            logger.info("🟢 Connected to MySQL database. Test query result: {}", result);
        } catch (Exception e) {
            logger.error("❌ Error connecting to MySQL database:", e);
        }
    }
}
