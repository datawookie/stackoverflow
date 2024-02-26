FROM php:8.2-fpm-bullseye

RUN pecl install xdebug-3.2.0 \
    && docker-php-ext-enable xdebug

RUN docker-php-ext-install mysqli pdo pdo_mysql

RUN apt-get update && \
    apt-get install -y \
    libzip-dev unzip \
    && docker-php-ext-install zip

RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
RUN chmod +x wp-cli.phar
RUN mv wp-cli.phar /usr/local/bin/wp
RUN wp --info

ENV COMPOSER_ALLOW_SUPERUSER=1

COPY composer.json .

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
# Allow the composer/installers plugin.
RUN composer config allow-plugins.composer/installers true
RUN composer update
