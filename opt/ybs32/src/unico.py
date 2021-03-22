#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import uvicorn
from fastapi import FastAPI

from logger import getLogger

app = FastAPI()
logger = getLogger()

@app.get("/do", status_code=200)
def do():
    logger.info("Hello")
    return {"message": "Hello"}

@app.get("/check", status_code=200)
def check():
    logger.error("Check")
    return {"message": "Check"}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
