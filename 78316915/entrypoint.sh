#!/usr/bin/env bash

set -e

RUN_MANAGE_PY='poetry run python project/manage.py'

echo 'Collect static files...'
$RUN_MANAGE_PY collectstatic --no-input

echo 'Running migrations...'
$RUN_MANAGE_PY migrate --no-input

echo 'Starting server...'
exec poetry run gunicorn project.config.wsgi:application --bind 0.0.0.0:8000
