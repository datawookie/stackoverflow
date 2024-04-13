FROM python:3.10-bookworm

WORKDIR /app

ENV POETRY_VERSION=1.8.1
ENV POETRY_VENV=/app/.venv

ENV PYTHONPATH=/app/project

ENV PATH="${POETRY_VENV}/bin:${PATH}:"

RUN python -m venv $POETRY_VENV && \
    pip install -U pip setuptools && \
    pip install poetry==${POETRY_VERSION}

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.in-project true && \
    poetry install --no-root

COPY project project

COPY entrypoint.sh ./entrypoint.sh
RUN chmod a+x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
