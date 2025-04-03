FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /opt/test_task

RUN apt-get update && apt-get install -y --no-install-recommends gcc \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip &&  \
    pip install poetry

RUN poetry config installer.max-workers 10 &&  \
    poetry install

COPY ./ ./

RUN useradd --create-home appuser
USER appuser