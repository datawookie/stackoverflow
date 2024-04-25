ARG PYTHON_VERSION=3.11-slim-buster
FROM python:${PYTHON_VERSION} as python

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app","--host", "0.0.0.0","--port", "8501"]
