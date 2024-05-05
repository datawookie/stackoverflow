FROM node:18.13.0 AS build

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install
COPY . .
# RUN npx expo export -p web

# FROM nginx:alpine

# COPY nginx.conf /etc/nginx/conf.d/default.conf
# COPY --from=build /app/dist /usr/share/nginx/html

# EXPOSE 8080
# CMD ["nginx", "-g", "daemon off;"]x
