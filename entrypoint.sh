#!/bin/bash

# Ejecuta las migraciones de Django
echo "Ejecutando migraciones..."
python manage.py migrate

# Inicia el servidor Gunicorn
echo "Iniciando servidor Gunicorn..."
gunicorn myproject.wsgi:application --bind 0.0.0.0:8000