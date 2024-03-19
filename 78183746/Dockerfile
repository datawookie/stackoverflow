FROM python:3.11.3

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y \
        wget \
        gnupg \
        unzip \
        xz-utils \
        build-essential \
        zlib1g-dev \
        libncurses5-dev \
        libgdbm-dev \
        libssl-dev \
        libreadline-dev \
        libffi-dev \
        libsqlite3-dev \
        libbz2-dev \
        libnss3-dev \
        openssl \
    && export DEBIAN_FRONTEND=noninteractive

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y \
    google-chrome-stable

RUN pip3 install --upgrade pip

RUN rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/

RUN pip3 install -r /tmp/requirements.txt

COPY run.py .

CMD python3 run.py
