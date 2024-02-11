FROM rocker/shiny

RUN rm -rf /srv/shiny-server/*

WORKDIR /srv/shiny-server/

COPY app.R ./
COPY files ./files
COPY www ./www
