FROM python:3.12.0-alpine3.18

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
