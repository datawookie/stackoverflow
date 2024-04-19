FROM --platform=linux/amd64 node:14.21.0-alpine as development

WORKDIR /home/app
COPY . /home/app

RUN apk add --no-cache --no-progress \
        python3 \
        make \
        g++ \
        libexecinfo-dev \
        libexecinfo

RUN npm install
