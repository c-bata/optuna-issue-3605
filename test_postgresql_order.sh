#!/bin/sh

echo "1. Prepare PostgreSQL 14.3 Server using Docker."
docker stop optuna-postgres

set -e
docker run \
  -d \
  --rm \
  -p 5432:5432 \
  --platform linux/x86_64 \
  -e POSTGRES_USER=root \
  -e POSTGRES_DB=optuna \
  -e POSTGRES_PASSWORD=root \
  --name optuna-postgres \
  postgres:14.3

echo "2. Run the order of trials"
python example.py

echo "3. Stop PostgreSQL Server"
docker stop optuna-postgres
