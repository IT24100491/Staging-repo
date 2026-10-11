import os

from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException

load_dotenv()

app = FastAPI()

API_KEY = os.getenv("API_KEY")


@app.get("/api/v1/health")
def health():
    return {"status": "ok"}


@app.get("/api/v1/data")
def get_data(x_api_key: str = Header(default="")):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    return {"status": "ok"}


@app.get("/api/v1/info")
def info():
    return {"service": "user-service", "environment": "staging", "version": "1.2.0"}


@app.get("/api/v1/users")
def get_users():
    return {"status": "not_implemented"}
