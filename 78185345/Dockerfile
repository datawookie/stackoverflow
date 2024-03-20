FROM node:18 as build-step

WORKDIR /app

COPY package*.json /app/

RUN npm install

COPY . /app

RUN npm run build -- --output-path=./dist
