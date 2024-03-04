FROM node:18-slim as base

ENV NODE_ENV=production

EXPOSE 3000

WORKDIR /app
RUN chown -R node:node /app

USER node

COPY --chown=node:node package*.json ./

RUN npm ci && npm cache clean --force

ENV PATH /app/node_modules/.bin:$PATH

COPY --chown=node:node . .

# STAGE: DEV ------------------------------------------------------------------

FROM base as dev

ENV NODE_ENV=development

CMD ["npm", "run", "start:dev"]

# STAGE: prod -----------------------------------------------------------------

FROM base as prod

RUN npm run build

CMD ["node", "dist/main.js"]
