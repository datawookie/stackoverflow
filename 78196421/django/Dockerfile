FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY django/ .

RUN ls

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "rac_backend.asgi:application", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
