#!/bin/sh

litestar database upgrade
uvicorn app.main:app --reload --host 0.0.0.0  --port 8000