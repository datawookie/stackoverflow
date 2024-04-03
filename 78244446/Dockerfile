FROM php:7.4-fpm-bullseye

RUN apt-get update && \
    apt-get install -y apache2

# To run PHP-FPM (in response to follow-up comment).
CMD php-fpm
