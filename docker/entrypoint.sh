#!/bin/sh

poetry run litestar --app app.main:app database upgrade
poetry run uvicorn app.main:app --reload --host 0.0.0.0  --port 8000