#!/bin/bash

# Your custom commands go here.
echo "* Hello, World!"

echo "* Content of mounted volume:"
ls /mnt

# Run original entrypoint.
exec docker-php-entrypoint apache2-foreground
