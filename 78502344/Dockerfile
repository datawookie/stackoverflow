FROM php:8.2-fpm

# Copy composer.lock and composer.json
# COPY composer.lock composer.json /var/www/

# Set working directory
WORKDIR /var/www

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpng-dev \
    libjpeg62-turbo-dev \
    libfreetype6-dev \
    locales \
    zip \
    jpegoptim optipng pngquant gifsicle \
    vim \
    unzip \
    git \
    curl \
    libonig-dev \
    libzip-dev \
    libgd-dev \
    procps
# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Update package list and install Nginx
RUN apt-get update && apt-get install -y nginx
# Remove default Nginx configuration
RUN rm /etc/nginx/sites-available/default

# Copy nginx.conf to /etc/nginx/sites-available as default


# Install extensions
RUN docker-php-ext-install pdo_mysql mbstring zip exif pcntl
RUN docker-php-ext-configure gd --with-external-gd
RUN docker-php-ext-install gd

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Copy Laravel application code
COPY . /var/www

COPY index.php /var/www/html/index.php

# Run composer update
# RUN composer update

# Run artisan commands
# RUN php artisan package:discover --ansi
# RUN php artisan optimize

# Change current user to www
# USER www

# Expose port 9000 and start php-fpm server
# CMD ["php-fpm"]

# Start Nginx server
# CMD ["nginx", "-g", "daemon off;"]

# RUN rm -f /etc/nginx/snippets/fastcgi-php.conf

COPY nginx.conf /etc/nginx/sites-available/default

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 80

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
