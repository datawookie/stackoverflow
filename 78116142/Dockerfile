FROM node:18.18-alpine3.18 As build

WORKDIR /usr/local/app

COPY package.json .

RUN npm install

COPY . /usr/local/app/

RUN npm run build
