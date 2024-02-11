FROM python:3.11.4-slim

RUN apt-get update -qq && apt-get install -qq -y curl

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY main.py .

CMD ["flask", "--app", "main", "run", "--host=0.0.0.0"]