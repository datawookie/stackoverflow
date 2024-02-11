FROM php:8.2.15-fpm

RUN apt update \
    && apt install -y git acl openssl openssh-client wget zip vim libssh-dev \
    && apt install -y libpng-dev zlib1g-dev libzip-dev libxml2-dev libicu-dev \
    && docker-php-ext-install intl pdo pdo_mysql zip

RUN apt install -y librabbitmq-dev \
    && pecl install amqp xdebug \
    && docker-php-ext-enable --ini-name 05-opcache.ini opcache amqp xdebug
