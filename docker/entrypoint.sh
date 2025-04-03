#!/bin/sh

# Задержка для базы данных
echo "Waiting for database to be ready..."
until nc -z -v -w30 db 5432; do
  echo "Waiting for database connection..."
  sleep 1
done

poetry run litestar --app app.main:app database upgrade

poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000