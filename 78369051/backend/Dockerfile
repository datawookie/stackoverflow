FROM python:3.10.12

WORKDIR /app

COPY backend/fastapi_app.py /app/
COPY requirements.txt /app/
COPY src/ /app/src
COPY setup.py /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "fastapi_app:app", "--host", "0.0.0.0", "--port", "8000"]
