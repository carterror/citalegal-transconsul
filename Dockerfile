FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /server

COPY requirements.txt .
# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# coping project files
COPY apps ./apps
COPY core ./core
COPY staticfiles ./staticfiles
COPY uploads ./uploads
COPY .env gunicorn-cfg.py manage.py start.sh ./

# gunicorn
CMD ["bash", "./start.sh"]
