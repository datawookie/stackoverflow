FROM python:3.11.7-slim

WORKDIR /app

RUN apt update

RUN apt install -y openssh-client

RUN python3 -m venv venv

RUN . venv/bin/activate

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./main.py ./main.py

COPY ./.env ./.env

CMD ["python3", "main.py"]
