# Stage 1
FROM python:3.12-slim as base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.8.3

WORKDIR /opt/test_task

RUN apt-get update && apt-get install -y --no-install-recommends gcc \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock* ./

RUN poetry config installer.max-workers 10 && \
    poetry install --no-dev --no-interaction --no-ansi

# Stage 2
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /opt/test_task

COPY --from=base /opt/test_task /opt/test_task

COPY ./ ./

RUN adduser --disabled-password --gecos "" appuser
USER appuser
