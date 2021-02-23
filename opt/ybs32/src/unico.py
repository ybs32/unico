#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/do", status_code=200)
def do():
    return {"message": "Hello"}

@app.get("/check", status_code=200)
def check():
    return {"message": "Hello"}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
