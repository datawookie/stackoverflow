# Use a base image that supports Python 2.7 (required for Django 1.6)
FROM ubuntu:16.04

# Create and set the working directory inside the container
WORKDIR /app

# Copy the project's requirements.txt file to the working directory
COPY requirements.txt /app

# Install some OS requirements
RUN apt-get update && \
    apt-get install -y wget build-essential git libpq-dev libxslt1-dev procps python \
    python-pip python-dev memcached libmemcached-tools postgresql-client apt-file zlib1g-dev \
    libjpeg-dev libxml2-dev libffi-dev libmysqlclient-dev

WORKDIR /app

COPY . /app

# Install project dependencies
RUN pip install --upgrade "pip < 21.0" && pip install virtualenv

# This will fail to complete
# RUN bash -c "pip install --no-cache-dir -r requirements.txt"

# This installs successfully
RUN bash -c "virtualenv /root/venv && source /root/venv/bin/activate && pip install --no-cache-dir -r requirements.txt"
