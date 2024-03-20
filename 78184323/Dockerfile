FROM selenium/standalone-chrome:latest

USER root

RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

WORKDIR /usr/src/app

COPY . .

RUN npm install

RUN chmod +x ./start.sh

USER seluser

CMD ["./start.sh"]
