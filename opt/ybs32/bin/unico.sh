#!/bin/bash

mkdir -p /var/log/gunicorn

BIND="-b 0.0.0.0:8000"
WORKERS="-w 1"
CLASS="-k worker.CustomUvicornWorker"
LOGGING="--log-config /etc/ybs32/gunicorn/logging.conf"

# Run
cd /opt/ybs32/src
/root/.pyenv/shims/gunicorn unico:app $BIND $WORKERS $CLASS $LOGGING
