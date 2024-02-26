FROM php:8.2-fpm-bullseye

RUN apt-get update -qq && \
    apt-get install -y -qq unzip

ENV COMPOSER_ALLOW_SUPERUSER=1

COPY composer.json .

RUN curl -sS https://getcomposer.org/installer | \
    php -- --install-dir=/usr/local/bin --filename=composer
# Allow the composer/installers plugin.
RUN composer config allow-plugins.composer/installers true
RUN composer update
