FROM python:3.12-bookworm

WORKDIR /usr/src/app

ENV POETRY_VERSION=1.8.1
ENV POETRY_VENV=/usr/src/app/.venv

ENV PATH="${POETRY_VENV}/bin:${PATH}:"

RUN python -m venv $POETRY_VENV && \
    pip install -U pip setuptools && \
    pip install poetry==${POETRY_VERSION}

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.in-project true && \
    poetry install --no-root

COPY . .

EXPOSE 8000

CMD uvicorn djadja.asgi:application --host 0.0.0.0 --port 8000
