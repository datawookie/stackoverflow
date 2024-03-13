FROM docker.io/library/postgres

RUN apt-get update && \
    apt-get install -y \
    cron \
    postgresql-`postgres -V | awk '{print $3}' | awk -F. '{print $1}'`-cron

COPY setup-pg-cron.sh /docker-entrypoint-initdb.d/

ENV POSTGRES_PASSWORD "password"
