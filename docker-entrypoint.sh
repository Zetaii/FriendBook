#!/bin/bash

# Wait for postgres to be ready
echo "Waiting for PostgreSQL to be ready..."
while ! pg_isready -h $DB_HOST -p $DB_PORT -q -U $DB_USER; do
  sleep 1
done

# Apply database migrations
echo "Applying database migrations..."
python src/manage.py migrate

# Start server
echo "Starting server..."
python src/manage.py runserver 0.0.0.0:8000 