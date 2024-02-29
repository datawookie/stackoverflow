# STAGE 1: WORDPRESS --------------------------------------------------------------------

FROM library/wordpress:php8.3-fpm-alpine AS build

RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar && \
    chmod +x wp-cli.phar && \
    mv wp-cli.phar /usr/local/bin/wp

RUN apk add --no-cache wget bash net-tools

COPY default/ /var/www/html/wp-content/themes/default/
COPY wp-install-plugins.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/wp-install-plugins.sh && \
    chown www-data:www-data /usr/local/bin/wp-install-plugins.sh

# STAGE 2: NGINX ------------------------------------------------------------------------

FROM nginx:stable-alpine AS nginx-server

RUN apk update && apk add --no-cache bash

RUN if ! getent group www-data >/dev/null; then addgroup -g 1000 www-data; fi

RUN adduser -D -H -u 1000 -G www-data -s /bin/bash www-data

COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY default/index.php /var/www/html/

COPY --from=build --chown=www-data:www-data /var/www/html/wp-content /var/www/html/wp-content

RUN find /var/www/html/wp-content -type f -exec chmod 644 {} \; && \
    find /var/www/html/wp-content -type d -exec chmod 755 {} \;

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
