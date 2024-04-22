FROM node:alpine AS builder

RUN apk add --update curl && \
    rm -rf /var/cache/apk/*

WORKDIR /usr/app

COPY ./package.json ./

RUN npm install

COPY ./index.js ./

FROM alpine

WORKDIR /usr/app

COPY --from=builder /usr/app .

RUN apk --no-cache add nodejs npm

RUN npm install express

EXPOSE 8080

ARG VERSION
ENV VERSION=production.${VERSION:-v1.0}

CMD ["node", "index.js"]
