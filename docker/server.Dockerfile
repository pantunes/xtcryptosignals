FROM python:3.7.2-alpine3.8

RUN python -m pip install --upgrade pip
RUN apk add --no-cache \
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

EXPOSE 5000 5001 5002

CMD xt-server --port 5000
CMD xt-server --port 5001
CMD xt-server --port 5002
