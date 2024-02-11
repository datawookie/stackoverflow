FROM gradle:7.6.1-jdk17-alpine

RUN export ALPINE_VERSION=$(cat /etc/alpine-release | cut -d "." -f 1-2) && \
    rm /etc/apk/repositories && \
    echo "https://dl-cdn.alpinelinux.org/alpine/v$ALPINE_VERSION/main" > /etc/apk/repositories && \
    echo "https://dl-cdn.alpinelinux.org/alpine/v$ALPINE_VERSION/community" >> /etc/apk/repositories

RUN apk add --no-cache \
        git \
        docker-cli \
        curl \
        libaio \
        libc6-compat \
        libnsl && \
    rm -rf /var/cache/apk/*
