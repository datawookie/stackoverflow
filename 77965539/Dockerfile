FROM node:21.6-alpine3.19

ENV NODE_ENV=production
RUN corepack enable

WORKDIR /app

COPY . .

RUN yarn install && \
    chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

CMD ["yarn", "start"]