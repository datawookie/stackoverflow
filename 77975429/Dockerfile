FROM python:3.11.4-slim

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY main.py .

CMD ["uvicorn", "main:app"]
