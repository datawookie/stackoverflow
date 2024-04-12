FROM python:3.10.0-alpine

RUN apk add postgresql-client build-base postgresql-dev

WORKDIR /movies_admin

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

COPY movies_admin .
