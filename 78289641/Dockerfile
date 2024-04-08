FROM node:18-alpine3.18

WORKDIR /app
COPY package.json .

RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

ENTRYPOINT ["node", "./dist/index.js"]
