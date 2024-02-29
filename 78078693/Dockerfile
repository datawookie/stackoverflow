# Stage 1: Build the WordPress application
FROM library/wordpress:php8.3-fpm-alpine AS build

# Install wp-cli
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar && \
    chmod +x wp-cli.phar && \
    mv wp-cli.phar /usr/local/bin/wp

# Use different mirrors
RUN sed -i -e 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories

# Install Postfix
RUN apk update && \
    apk add --no-cache postfix && \
    postconf -e myhostname=mydomain.com && \
    postconf -e relayhost="mailfwd.mydomain.com" && \
    postfix start && \
    postfix reload

# Configure PHP and create directory if it doesn't exist
RUN mkdir -p /usr/local/etc/php/conf.d/ && \
    echo "sendmail_path=sendmail -t -i" >> /usr/local/etc/php/conf.d/sendmail.ini

# Install packages: wget, bash
RUN apk add --no-cache wget bash

# Install net-tools
RUN apk add --no-cache net-tools

# Copy built files to WordPress files system
COPY default/ /var/www/html/wp-content/themes/default/

# Set permissions for the wp-install-plugins.sh script
COPY wp-install-plugins.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/wp-install-plugins.sh

# Grant permissions to the www-data user
RUN chown www-data:www-data /usr/local/bin/wp-install-plugins.sh


# Stage 2: Build the NGINX server
FROM nginx:stable-alpine AS nginx-server

# Install bash in current image
RUN apk update && apk add --no-cache bash

# Check if www-data group exists, if not, add it
RUN if ! getent group www-data >/dev/null; then addgroup -g 1000 www-data; fi

# Add www-data user with existing www-data group
RUN adduser -D -H -u 1000 -G www-data -s /bin/bash www-data

# Copy the NGINX configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy default index.php file
COPY default/index.php /var/www/html/

# Copy static content from WordPress build stage
COPY --from=build --chown=www-data:www-data /var/www/html/wp-content /var/www/html/wp-content

# Set permissions for static content
RUN find /var/www/html/wp-content -type f -exec chmod 644 {} \; && \
    find /var/www/html/wp-content -type d -exec chmod 755 {} \;

# Expose port 80 to allow incoming connections
EXPOSE 80

# Command to start NGINX when the container starts
CMD ["nginx", "-g", "daemon off;"]
