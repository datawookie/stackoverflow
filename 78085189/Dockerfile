FROM php:7.2.1-fpm AS php

WORKDIR /usr/share/nginx/html

COPY web/index.php /usr/share/nginx/html
COPY config/php.ini /usr/local/etc/php/php.ini

EXPOSE 8000
