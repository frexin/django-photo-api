FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /srv/www/photoapi
WORKDIR /srv/www/photoapi

COPY ./app /srv/www/photoapi
RUN pip install -r requirements.txt