package com.example.demo.config;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.stereotype.Component;

@Component
public class RedisConnectionCheck implements CommandLineRunner {

    private static final Logger logger = LoggerFactory.getLogger(RedisConnectionCheck.class);

    // Inject the Redis host and port from application.properties
    @Value("${spring.redis.host}")
    private String redisHost;

    @Value("${spring.redis.port}")
    private int redisPort;

    private final StringRedisTemplate redisTemplate;

    public RedisConnectionCheck(StringRedisTemplate redisTemplate) {
        this.redisTemplate = redisTemplate;
    }

    @Override
    public void run(String... args) {
        logger.info("🔴 Making connection to Redis at {}:{}.", redisHost, redisPort);

        // Perform a simple operation to check Redis connection
        String key = "redis_connection_test";
        String value = "success";
        redisTemplate.opsForValue().set(key, value);

        // If the above operation did not throw an exception, assume connected
        logger.info("🟢 Connected to Redis at {}:{}.", redisHost, redisPort);
    }
}
