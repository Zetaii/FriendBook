#!/bin/bash

# Wait for postgres to be ready
echo "Waiting for PostgreSQL to be ready..."
while ! pg_isready -h $DB_HOST -p $DB_PORT -q -U $DB_USER; do
  sleep 1
done

# Apply database migrations
echo "Applying database migrations..."
python src/manage.py migrate

# Create superuser if it doesn't exist
echo "Creating superuser..."
python src/manage.py shell << END
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
END

# Start server
echo "Starting server..."
python src/manage.py runserver 0.0.0.0:8000