#!/bin/sh
FROM alpine:3.8

# RUN apk update && apk add bash nano curl \
RUN apk update && apk add bash nano curl \
        gcc \
        musl-dev \
        zlib-dev \
        python3 \
        python3-dev \
        uwsgi-python3 \
        libpq \
        gettext

RUN addgroup -S django && adduser -S -G django django
RUN mkdir -p /usr/src/app/mysite
WORKDIR /usr/src/app

ARG PROJECT
ADD ${PROJECT}/setup.py \
    ${PROJECT}/requirements.txt \
    /usr/src/app/
RUN pip3 install -U setuptools && pip3 install -U -e .
COPY ${PROJECT} /usr/src/app/

ENV DJANGO_SETTINGS_MODULE mysite.settings.local

COPY configs/uwsgi-entrypoint.ini /configs/
VOLUME /usr/src/app
EXPOSE 8001
CMD [ "uwsgi", "--ini", "/configs/uwsgi-entrypoint.ini" ]