#!/bin/sh

set -e

echo "Warte auf PostgreSQL auf $DB_HOST:$DB_PORT..."

while ! pg_isready -h "$DB_HOST" -p "$DB_PORT" -q; do
  echo "PostgreSQL is not reachable - sleep 1 seconds..."
  sleep 1
done

echo "PostgreSQL is ready - go foward..."

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate

python manage.py shell <<EOF
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'adminpassword')

if not User.objects.filter(username=username).exists():
    print(f"Creating superuser '{username}'...")
    # Korrekter Aufruf: username hier übergeben
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser '{username}' created.")
else:
    print(f"Superuser '{username}' already exists.")
EOF

if [ "$DJANGO_MODE" = "worker" ]; then
  echo "Starte RQ Worker..."
  exec python manage.py rqworker default
else
  echo "Starte Webserver..."
  exec python manage.py runserver 0.0.0.0:8000
fi
