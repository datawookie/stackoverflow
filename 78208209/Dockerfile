FROM python:3.12-slim AS builder

ENV POETRY_HOME=/opt/poetry \
    POETRY_VERSION=1.8.2 \
    PATH="/opt/poetry/bin:$PATH"

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        build-essential \
    && rm -rf /var/lib/apt/lists/* && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    poetry config virtualenvs.create false

WORKDIR /app/

# =============================================================================

FROM builder as data_sources_builder

COPY data_sources/pyproject.toml data_sources/poetry.lock .

RUN poetry install

COPY data_sources/ .

RUN poetry build

# =============================================================================

FROM builder AS api_builder

COPY api/pyproject.toml api/poetry.lock .

RUN poetry install

COPY api/ .

RUN poetry build

# =============================================================================

FROM python:3.12-slim

COPY --from=data_sources_builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=api_builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=api_builder /usr/local/bin/uvicorn /usr/local/bin/

WORKDIR /app/

COPY . .

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
