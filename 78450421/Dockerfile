FROM node:22-alpine

ENV NODE_ENV production

WORKDIR /usr/web-server

RUN npm i -g @nestjs/cli typescript

COPY ./package*.json ./
RUN npm install
RUN npm install @types/node

COPY ./ ./

EXPOSE 4000

CMD npm run start:dev
