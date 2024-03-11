FROM node:20
WORKDIR /app

ARG NEXT_PUBLIC_BACKEND_BASE_URL
ENV NEXT_PUBLIC_BACKEND_BASE_URL=$NEXT_PUBLIC_BACKEND_BASE_URL

COPY package.json .
COPY .npmrc .npmrc
RUN npm i
COPY . .

RUN npm run build

CMD [ "npm", "start" ]
