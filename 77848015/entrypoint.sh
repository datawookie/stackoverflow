#!/bin/sh

echo "Waiting for PostgreSQL..."

while ! nc -z db 5432; do
  echo "..."
  sleep 0.1
done

echo "PostgreSQL started."
