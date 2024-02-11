FROM wordpress:php8.2

RUN apt update -q && \
    apt install -q -y libpq-dev && \
    docker-php-ext-install pdo_pgsql pgsql
