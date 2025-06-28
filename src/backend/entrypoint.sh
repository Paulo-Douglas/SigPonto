#!/bin/sh

set -e

python manage.py migrate

python manage.py init_data

python manage.py runserver 0.0.0.0:8000