FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y \
        wget \
        build-essential \
        git \
        libpq-dev \
        libxslt1-dev \
        procps \
        python \
        python-pip \
        python-dev \
        memcached \
        libmemcached-tools \
        postgresql-client \
        apt-file \
        zlib1g-dev \
        libjpeg-dev \
        libxml2-dev \
        libffi-dev \
        libmysqlclient-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade "pip < 21.0"

RUN pip install setuptools==44.1.1
RUN pip install -r requirements.txt
