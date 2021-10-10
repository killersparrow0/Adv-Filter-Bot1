#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("4080786"))

API_HASH = os.environ.get("b214aec132378022e02df812714ba7a4")

BOT_TOKEN = os.environ.get("2057444955:AAG6jrqydNl1adP5bhs2sCTNzZdVWX_u33k")

DB_URI = os.environ.get("mongodb+srv://elonmuskme:elonmuskme@filter.nqwqi.mongodb.net/Filter?retryWrites=true&w=majority")

USER_SESSION = os.environ.get("BQA-BScxKd98r5cD_48j3bLX_-VJCuQJxpn-DXPO3XQ3vCvkVwp8NHd38E1OyYsJfK1mflRQHNLtCEa6OpNPozkB3Xnac16WhEAllAs3ER1CKUoyLMAHEasHmbiPSXwNWI3Eu_FOOuHaiPTOsduXUgW4kzjWrNInhNkGilGJj1dKd9kfJSZmhLGpT4xjno-v4d2C95mpk_kisCPw6Gg6r1q5g8pjomyL6-wacB2v1l8VTeOL6vCt04MC6VydqJKnmGoJEkPPnGytVwZZACRWWqvBOwwwlLg2E0MhXXh_GDIDai7yLNsnN6O66itflYPp0Nb65mCoVvDAZVTLmiNomN8lZIG7kAA")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
