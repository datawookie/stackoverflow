FROM node:18.17.0-alpine as base

WORKDIR /app

COPY next.config.js package.json .
COPY pages/ ./pages

RUN npm install --frozen-lockfile
RUN npm run build

ENV NODE_OPTIONS="--inspect=0.0.0.0:9229"

CMD npm start
