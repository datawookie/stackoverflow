FROM node:latest as build

WORKDIR /usr/local/app

COPY package.json .

RUN npm install

COPY . .

CMD ["npm", "start"]
