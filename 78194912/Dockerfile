# =============================================================================

FROM node:16.16.0-alpine AS build

RUN apk add --update --no-cache \
    python3 \
    make \
    g++

COPY . /src

WORKDIR /src

RUN npm install

RUN apk update && apk add bash

RUN npm run build
RUN npm run test:unit

RUN npm prune --production

# =============================================================================

FROM node:16.16.0-alpine

RUN apk add --update --no-cache curl

EXPOSE 3000

WORKDIR /usr/src/service

COPY --from=build ./src/node_modules node_modules
COPY --from=build ./src/dist dist

HEALTHCHECK --interval=5s \
            --timeout=5s \
            --retries=6 \
            CMD curl -fs http://localhost:3000/ || exit 1

USER node

ENV TZ UTC

CMD ["node", "./dist/index.js"]
