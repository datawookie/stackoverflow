FROM python:3.10

WORKDIR /code

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY speech.py .

CMD python3 speech.py
