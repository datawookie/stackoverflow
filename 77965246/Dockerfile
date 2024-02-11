FROM node:18-bullseye-slim

RUN apt-get update;DEBIAN_FRONTEND=noninteractive apt-get install -yq git bash jq build-essential python python3-pip openssl pkg-config;apt-get clean

ARG EDUMEET_SERVER
ARG SERVER_MANAGEMENT_USERNAME
ARG SERVER_MANAGEMENT_PASSWORD

RUN git clone --single-branch --branch main https://github.com/edumeet/edumeet-docker.git

WORKDIR /edumeet-docker

# COPY  configs/server/config.json /edumeet-docker/config/config.json

# RUN mv  /app/${EDUMEET_SERVER}/ /usr/src/app/

# WORKDIR /usr/src/app

RUN yarn install
# RUN yarn run build

# EXPOSE 8443

# ARG SERVER_DEBUG

# ENTRYPOINT DEBUG=${SERVER_DEBUG} MANAGEMENT_USERNAME=${SERVER_MANAGEMENT_USERNAME} MANAGEMENT_PASSWORD=${SERVER_MANAGEMENT_PASSWORD} yarn run prodstart $0 $@
