FROM python:3.7.2-alpine3.8

RUN python -m pip install --upgrade pip
RUN apk add --no-cache \
    alpine-sdk \
    zlib \
    libjpeg-turbo-dev \
    libpng-dev \
    freetype-dev \
    lcms2-dev \
    libwebp-dev \
    harfbuzz-dev \
    fribidi-dev \
    tcl-dev \
    tk-dev \
    openssl-dev \
    libffi-dev \
    gcc \
    python3-dev \
    musl-dev \
    bash

WORKDIR /xtcryptosignals

ADD ./ ./

RUN pip install -r requirements.txt
RUN pip install -e .

ENV FLASK_ENV=docker
ENV SETTINGS_APP=/xtcryptosignals/xtcryptosignals/config/server.docker.env
