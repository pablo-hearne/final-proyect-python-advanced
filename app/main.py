from fastapi import FastAPI
from app.models.clients import Client

app = FastAPI()


@app.get("/")
def root():
    return {"Hello":"World"}

@app.get("/clients")
def get_clients():
    return