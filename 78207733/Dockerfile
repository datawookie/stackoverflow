FROM node:20.11.1-alpine as base

RUN apk add --no-cache \
        libxkbcommon \
        dbus \
        ttf-freefont \
        udev \
        xvfb \
        zlib \
        chromium \
        chromium-chromedriver \
        nss \
        freetype \
        freetype-dev \
        harfbuzz \
        ca-certificates \
    && rm -rf /var/cache/apk/*

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

# FROM base
# ENV NODE_ENV=production
# WORKDIR /app
# COPY --from=production-deps /app/node_modules /app/node_modules
# COPY --from=build /app/build /app
# EXPOSE 3333
# CMD ["node", "./bin/server.js"]
