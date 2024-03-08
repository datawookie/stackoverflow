FROM node:lts-slim

RUN npm i npm@latest -g

# USER node

WORKDIR /opt/node_app

COPY package*.json .

# # RUN --mount=type=secret,id=TOKEN \
# #     TOKEN=<placeholder> && \
# #     echo //npm.pkg.github.com/:_authToken=${TOKEN} >> ~/.npmrc && \
# #     echo @${OWNER}:registry=https://npm.pkg.github.com/ >> ~/.npmrc && \
# #     npm ci && npm cache clean --force


RUN npm ci
ENV PATH /opt/node_app/node_modules/.bin:$PATH

WORKDIR /opt/node_app/app
COPY --chown=node:node src/ src/
RUN npm run build

CMD ["npm", "run", "start"]
