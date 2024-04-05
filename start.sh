#!/bin/bash

# Executing migration before the project
python3 manage.py migrate

# Executing the project
python3 manage.py runserver 0.0.0.0:80
