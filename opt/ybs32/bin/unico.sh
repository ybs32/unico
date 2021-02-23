#!/bin/bash

cd /opt/ybs32/src/
/root/.pyenv/shims/gunicorn -w 1 -k worker.CustomUvicornWorker unico:app --bind 0.0.0.0:8000
