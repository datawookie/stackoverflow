FROM php:8.1.0-apache

RUN a2enmod rewrite
RUN apt-get update -y && apt-get install -y \
    libicu-dev \
    libmariadb-dev \
    unzip zip \
    zlib1g-dev \
    libpng-dev \
    libjpeg-dev \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libpng-dev
RUN docker-php-ext-install gettext intl pdo_mysql gd

WORKDIR /app
COPY . /app

COPY --from=composer:latest /usr/bin/composer /usr/bin/composer
RUN composer install --no-interaction -vvv

RUN pecl install xdebug \
    && docker-php-ext-enable xdebug

EXPOSE 8000
