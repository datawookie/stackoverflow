FROM node:21.7.3-bullseye-slim

WORKDIR /app

COPY ./package*.json .

RUN npm install

COPY . .

CMD ["npm", "run", "dev"]
