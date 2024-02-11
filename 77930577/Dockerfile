FROM node:14

WORKDIR /usr/app

COPY package*.json ./

RUN npm install

RUN mkdir -p data

COPY . .

CMD ["node", "app.js"]
