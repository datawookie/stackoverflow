FROM node:20.10 as build-stage

ARG ENV_FILE
ENV ENV_FILE=${ENV_FILE}

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

RUN cp ${ENV_FILE} .env && \
    npm run build

FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
