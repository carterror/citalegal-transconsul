#!/bin/bash

# Executing migration before the project
python3 manage.py migrate

# Executing the project
gunicorn --config gunicorn-cfg.py configs.wsgi
