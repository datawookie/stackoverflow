FROM postgres:16.2-alpine

ENV POSTGRES_DB ""
ENV POSTGRES_USER ""
ENV POSTGRES_PASSWORD ""
ENV POSTGRES_CONF ""
ENV PATH="/usr/pgsql-16/bin:${PATH}"

ARG PG_PARTMAN_VERSION
ARG PG_CRON_VERSION
ARG PG_GIS_VERSION
ARG USER="data-pipeline"

RUN apk add --no-cache postgresql-pg_cron="${PG_CRON_VERSION}-r0" --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community \
    && apk add --no-cache postgresql-pg_partman="${PG_PARTMAN_VERSION}-r0" --repository=http://dl-cdn.alpinelinux.org/alpine/edge/testing \
    && apk add --no-cache postgis="${PG_GIS_VERSION}-r0" --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community \
    && cp /usr/share/postgresql/extension/* /usr/local/share/postgresql/extension/
# Tried to copy the .so file but that didn't solve my issue.
#RUN cp -r /usr/lib/postgresql16/ usr/local/lib/postgresql/


# Question: Why do we need this entry point if we've already installed the extensions?
# Answer: PostgreSQL needs to be running in order to install extensions and
#         we can't start PostgreSQL until after we're done building the container
#         So we're chosing to add scripts to run on container start to circumvent
#         the chicken or egg problem.
# Copy in the load-extensions script
COPY db/initdb_scripts /docker-entrypoint-initdb.d/
