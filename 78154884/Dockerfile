FROM postgres:latest

ENV POSTGRES_DB ""
ENV POSTGRES_USER ""
ENV POSTGRES_PASSWORD ""

RUN apt-get update -q && \
    apt-get install -q -y git make gcc libkrb5-dev postgresql-server-dev-16

WORKDIR /usr/share/postgresql/16/contrib

ENV USE_PGXS=1

RUN git clone https://github.com/EnterpriseDB/pldebugger.git && \
    cd pldebugger && \
    make

COPY setup-pg-admin.sh /docker-entrypoint-initdb.d/
