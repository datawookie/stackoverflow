FROM --platform=linux/amd64 node:12.15.0-alpine as development

WORKDIR /home/app
COPY . /home/app

RUN apk add --no-cache --no-progress \
        python \
        make \
        g++ \
        libexecinfo-dev \
        libexecinfo

RUN npm install
