FROM python:3.10.12-slim

WORKDIR /app

COPY requirements.txt /app

RUN apt-get update -y && \
    apt-get install -y postgresql postgresql-contrib && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache && \
    apt-get autoremove -y

ENV PYTHONUNBUFFERED=1

COPY main.py /app
# NOTE: You should not copy the .env file into the image. This is for illustration only!
COPY .env /app

CMD ["python", "main.py"]
