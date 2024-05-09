FROM node:22-alpine

ENV NODE_ENV production

WORKDIR /usr/web-server

COPY ./package*.json ./
RUN npm install

COPY ./ ./

EXPOSE 4000

CMD npm run start:dev
