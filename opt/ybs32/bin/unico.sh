#!/bin/bash

cd /opt/ybs32/src/
/root/.pyenv/shims/gunicorn -w 1 -k worker.CustomUvicornWorker unico:app --bind 127.0.0.1:8000
