FROM --platform=linux/amd64 python:3.7-buster

RUN apt-get update --fix-missing && apt-get install --no-install-recommends -y \
        ca-certificates \
        curl \
        gnupg \
        libglib2.0-0\
        libxext6 \
        libsm6 \
        libxrender1 \
        build-essential \
        apt-transport-https \
        rsyslog \
        logrotate \
        unixodbc \
        unixodbc-dev

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /usr/src

COPY prepare.py .

ENTRYPOINT ["python3", "prepare.py"]
