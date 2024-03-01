# STAGE 1: PHP --------------------------------------------------------------------------

FROM php:7.2.1-fpm AS php

COPY web/index.php /usr/share/nginx/html
COPY config/php.ini /usr/local/etc/php/php.ini

# STAGE 2: NGINX ------------------------------------------------------------------------

FROM nginx:stable-alpine AS nginx

RUN apk update && apk add --no-cache bash

RUN if ! getent group www-data >/dev/null; then addgroup -g 1000 www-data; fi

RUN adduser -D -H -u 1000 -G www-data -s /bin/bash www-data

COPY nginx.conf /etc/nginx/conf.d/default.conf

# COPY --from=build --chown=www-data:www-data /var/www/html/wp-content /var/www/html/wp-content

# RUN find /var/www/html/wp-content -type f -exec chmod 644 {} \; && \
#     find /var/www/html/wp-content -type d -exec chmod 755 {} \;

# EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
