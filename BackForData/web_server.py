import json
import urllib

import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_main():
    return {
        "routes": [
            {"method": "GET", "path": "/", "summary": "Landing"},
            {"method": "GET", "path": "/status", "summary": "App status"},
        ]
    }

@app.get("/status")
def get_status():
    return {"status": "ok"}
