FROM python:3.12-bookworm

ENV POETRY_VERSION=1.8.1

RUN pip install -U pip setuptools && \
    pip install poetry==${POETRY_VERSION}

ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR /usr/src/app

COPY pyproject.toml .

RUN poetry config virtualenvs.create false && poetry install --no-root

COPY . .

EXPOSE 8000

CMD ["uvicorn", "djadja.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
