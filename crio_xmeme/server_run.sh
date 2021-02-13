#!/bin/sh
ls

python manage.py migrate
make build 
make compose-start