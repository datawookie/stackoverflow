package com.example.demo.config;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.jdbc.datasource.DriverManagerDataSource;
import org.springframework.stereotype.Component;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.ResultSet;

@Configuration
public class DatabaseConfig {
    private static final Logger logger = LoggerFactory.getLogger(DatabaseConfig.class);

    @Bean
    public DataSource dataSource() {
        DriverManagerDataSource dataSource = new DriverManagerDataSource();
        dataSource.setDriverClassName("com.mysql.cj.jdbc.Driver");
        dataSource.setUrl("jdbc:mysql://mysql:3306/oks");
        dataSource.setUsername("root");
        dataSource.setPassword("roots");
        return dataSource;
    }

    @Component
    public static class MySqlConnectionCheck implements CommandLineRunner {

        private final DataSource dataSource;

        public MySqlConnectionCheck(DataSource dataSource) {
            this.dataSource = dataSource;
        }

        @Override
        public void run(String... args) {
            logger.info("Making connection to MySQL database.");
            try (Connection connection = dataSource.getConnection()) {
                String query = "SELECT 1";
                ResultSet rs = connection.createStatement().executeQuery(query);
                if (rs.next()) {
                    int result = rs.getInt(1);
                    logger.info("🟢 Connected to MySQL database. Test query result: {}", result);
                }
            } catch (Exception e) {
                logger.error("❌ Error connecting to MySQL database: ", e);
            }
        }
    }
}
