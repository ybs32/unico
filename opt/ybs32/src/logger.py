#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import logging
from pytz import timezone
from pythonjsonlogger import jsonlogger


class JsonFormatter(jsonlogger.JsonFormatter):

    def parse(self):
        return [
            'timestamp',
            'level',
            'message',
        ]

    def add_fields(self, record, rec, message_dict):
        super().add_fields(record, rec, message_dict)

        if not record.get('timestamp'):
            zone = timezone('Asia/Tokyo')
            format = '%Y-%m-%dT%H:%M:%S%z'
            record['timestamp'] = datetime.datetime.now(zone).strftime(format)

        if record.get('level'):
            record['level'] = record['level'].upper()
        else:
            record['level'] = rec.levelname


def getLogger():
    handler = logging.handlers.TimedRotatingFileHandler(
        filename = "/var/log/unico/general.log",
        when = "midnight",
        interval = 1,
        backupCount = 90,
        encoding = "utf-8"
    )
    handler.setFormatter(JsonFormatter())
    logger = logging.getLogger("")
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger
