FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src

RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/src/

RUN mkdir -p /app/src/users/management/commands

COPY src/users/management/commands/init_db.py /app/src/users/management/commands/

WORKDIR /app/src

EXPOSE 8080

CMD python manage.py init_db && gunicorn friendbook.wsgi:application --bind 0.0.0.0:8080