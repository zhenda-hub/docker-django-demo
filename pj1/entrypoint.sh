#!/bin/bash

echo "start sh!!!!!!!"
# ls
# pwd
# whoami
# pip list

# pip freeze > requirements.txt
# django-admin startproject pj1

python manage.py migrate
python manage.py collectstatic --noinput

# python manage.py runserver 0.0.0.0:8000
gunicorn -c gunicorn_conf.py pj1.wsgi

tail -f /dev/null
# sleep infinity