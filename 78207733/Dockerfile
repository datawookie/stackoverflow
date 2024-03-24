FROM node:20.11.1 as base

RUN apt-get update -q && \
    apt-get install -q -y \
        libasound2 \
        libatk-bridge2.0-0 \
        libgtk-4-1 \
        libnss3 \
        xdg-utils

# =============================================================================

FROM base as deps
WORKDIR /app
COPY package.json .
RUN npm install

# =============================================================================

FROM base as build
WORKDIR /app
COPY --from=deps /app/node_modules /app/node_modules
COPY . .
RUN npm run build

# =============================================================================

FROM base
ENV NODE_ENV=production
WORKDIR /app
COPY --from=deps /app/node_modules /app/node_modules
COPY --from=deps /root/.cache/ /root/.cache/
COPY --from=build /app/build /app/bin
EXPOSE 3333
CMD ["node", "./bin/server.js"]
