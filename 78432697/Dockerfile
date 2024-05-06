FROM python:3.11 AS python

FROM alpine:latest AS alpine

COPY --from=python /usr/local/bin/python /usr/local/bin/python

FROM node:20 AS node

COPY --from=alpine /usr/local/bin/python /usr/local/bin/python
