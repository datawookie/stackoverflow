FROM python:3.11 AS backend-build

COPY backend /app/backend

WORKDIR /app/backend

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "-m", "quart", "--app", "main:app", "run", "--host", "0.0.0.0", "--reload"]