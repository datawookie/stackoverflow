FROM python:3.8.0-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libopencv-dev

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt
