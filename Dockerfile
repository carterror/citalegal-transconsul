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
COPY blog ./blog
COPY citas ./citas
COPY usuarios ./usuarios
COPY templates ./templates
COPY configs ./configs
COPY media ./media
COPY static ./static

COPY gunicorn-cfg.py manage.py start.sh ./

# gunicorn
CMD ["bash", "./start.sh"]
