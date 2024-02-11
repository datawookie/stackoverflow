FROM ubuntu:23.04

RUN apt-get update -qq -y && apt-get install -qq -y curl libicu-dev
RUN curl -Lo bicep https://github.com/Azure/bicep/releases/download/v0.23.1/bicep-linux-x64 && \
    chmod +x bicep && \
    mv bicep /usr/local/bin/bicep
