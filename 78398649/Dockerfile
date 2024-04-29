FROM node:latest as build

WORKDIR /usr/local/app

COPY package.json .
RUN npm install
RUN npm install @angular/cli@17

COPY . .

EXPOSE 4200
CMD ["npm", "start"]
