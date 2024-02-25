#!/bin/bash

docker volume create vol1-db-vol
docker volume create vol2-db-vol

docker run -d --name db1 \
    -e MYSQL_ROOT_PASSWORD=dbadmin \
    -v vol1-db-vol:/var/lib/mysql \
    mariadb:10.6.17-focal

docker run -d --name db2 \
    -e MYSQL_ROOT_PASSWORD=dbadmin \
    -e MYSQL_TCP_PORT=3307 \
    -v vol2-db-vol:/var/lib/mysql \
    mariadb:10.5.24-focal

docker run -d --name myadmin1 \
    -e PMA_HOST=db1 \
    -p 8080:80 \
    phpmyadmin:latest

docker run -d --name myadmin2 \
    -e PMA_HOST=db2 \
    -e PMA_PORT=3307 \
    -p 8081:80 \
    phpmyadmin:latest
