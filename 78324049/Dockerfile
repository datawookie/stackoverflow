FROM rust:1.77-alpine3.18 as builder

WORKDIR /app
COPY . /app

RUN rustup default stable

# Probably not necessary, but just to be safe.
#
ENV OPENSSL_LIB_DIR=/usr/lib
ENV OPENSSL_INCLUDE_DIR=/usr/include

RUN apk update && \
    apk add --no-cache \
        build-base \
        libpq \
        musl-dev \
        pkgconfig \
        openssl-dev \
        postgresql-dev \
        libc6-compat

RUN cargo build --release
