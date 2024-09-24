FROM python:3.11

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 80
WORKDIR .

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