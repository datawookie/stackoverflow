FROM python:3.11

RUN apt-get update && \
    apt-get install -y wget unzip && \
    apt-get clean

WORKDIR /app

ENV TZ="America/Los_Angeles"
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

COPY . /app

CMD ["python", "bot.py"]
