#!/bin/bash

# Executing migration before the project
python3 manage.py migrate

# Executing the project
gunicorn configs/wsgi.py
