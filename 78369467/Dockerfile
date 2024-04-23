FROM python:3.12.0 AS base

COPY requirements.txt .
COPY test.py .
COPY another-test.py .

COPY foo/ /app/foo/

FROM ubuntu:latest

COPY --from=base requirements.txt .
