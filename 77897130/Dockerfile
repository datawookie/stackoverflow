FROM node:18.18-alpine3.18 As build

WORKDIR /usr/local/app
COPY package*.json ./

RUN npm install

COPY ./ /usr/local/app/

ARG ENVIRONMENT=production

RUN npm run build -- --configuration=${ENVIRONMENT}

# FROM nginx:latest

# COPY --from=build /usr/local/app/dist/angular-app /usr/share/nginx/html

# RUN sed -i s#MY_APP_API_URL#$API_URL#g /usr/share/nginx/html/main.*.js

# COPY --from=build /usr/local/app/nginx.conf /etc/nginx/conf.d/default.conf

# EXPOSE 80
