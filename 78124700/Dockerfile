FROM node:lts-slim

RUN npm i npm@latest -g

WORKDIR /opt/app

COPY package*.json .

RUN npm ci
ENV PATH /opt/node_app/node_modules/.bin:$PATH

COPY --chown=node:node src/ src/

RUN npm run build

CMD ["npm", "run", "start"]
