FROM node:current-alpine3.19

WORKDIR /usr/src/app

RUN chown -R node:node /usr/src/app

COPY src/package.json .
COPY src/package-lock.json .

RUN npm install

USER node

COPY --chown=node:node ./src .

CMD [ "npm", "start" ]
