#!/bin/bash

mkdir -p /var/log/gunicorn

# OPTIONS
BIND="-b 0.0.0.0:8000"
WORKER="-w 1 -k worker.CustomUvicornWorker"
LOGGING="--log-config /etc/ybs32/gunicorn/logging.conf"
PROC_NAME="--name unico" # for Datadog
STATSD="--statsd-host 127.0.0.1:8125" # for Datadog

# Run
cd /opt/ybs32/src
/root/.pyenv/shims/gunicorn unico:app $BIND $WORKER $LOGGING $PROC_NAME $STATSD
