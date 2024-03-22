FROM node:lts-alpine as base

RUN npm install -g pnpm

WORKDIR /usr/src/app

COPY package.json pnpm-lock.yaml ./

RUN pnpm install

COPY . .

RUN pnpm run build

FROM node:lts-alpine as final

WORKDIR /app

COPY --from=base /usr/src/app/.output .

EXPOSE 3000

CMD ["node", "server/index.mjs"]
