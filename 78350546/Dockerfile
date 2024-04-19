FROM --platform=linux/amd64 node:15.14.0-alpine3.13 as development

WORKDIR /home/app
COPY package.json /home/app

RUN apk add --no-cache --no-progress \
        python3 \
        make \
        g++ \
        libexecinfo-dev \
        libexecinfo

RUN npm install
