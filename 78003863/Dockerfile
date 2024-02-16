FROM node:16-buster AS frontend-build

COPY frontend /app/frontend

WORKDIR /app/frontend

RUN rm -r node_modules

RUN npm install

RUN npm run build

FROM python:3.11 AS backend-build

COPY backend /app/backend

WORKDIR /app/backend

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "-m", "quart", "--app", "main:app", "run", "--port", "5000", "--host", "localhost", "--reload"]