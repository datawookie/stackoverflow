FROM python:3.12-alpine3.19
LABEL maintainer="Matheus Tenório"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    pip install -r requirements.txt && \
    rm -f requirements.txt && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
    djangouser && \
    chown djangouser:djangouser -R /app/

COPY app /app

USER djangouser

RUN python manage.py migrate

CMD python manage.py runserver 0.0.0.0:8000
