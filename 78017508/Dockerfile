FROM node:20

RUN apt-get -y update \
    && apt-get install -y ffmpeg \
    && ffmpeg -version && which ffmpeg

WORKDIR /usr/src/app

COPY . .

RUN npm install && npm install -g typescript
RUN tsc

WORKDIR /usr/src/app/responder

CMD ["node", "main.js"]
