# -*- coding: utf-8 -*-
"""
Created By Murray(m18527) on 2019/12/13 13:57
"""
from __future__ import absolute_import, unicode_literals

import logging
import os
from logging.handlers import RotatingFileHandler

LOG_PATH = os.getenv("LOG_FILE_PATH", "/var/log/")
LOG_FILE_NAME = os.getenv("LOG_FILE_NAME", "surge")
os.makedirs(LOG_PATH, exist_ok=True)

log_file = os.path.join(LOG_PATH, '{}.log'.format(LOG_FILE_NAME))
LOG_LEVEL = getattr(logging, str(os.getenv("LOG_LEVEL", "INFO")).upper(), logging.INFO)

console = logging.StreamHandler()
console.setLevel(LOG_LEVEL)

rotating_file_handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024 * 10, backupCount=10, encoding='utf8')
rotating_file_handler.setLevel(LOG_LEVEL)

logging.basicConfig(
    level=LOG_LEVEL,
    format='%(asctime)s.%(msecs)d - %(levelname)-8s - [%(filename)s:%(lineno)d][%(funcName)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[rotating_file_handler, console]
)