from fastapi import HTTPException
from app.repositories.database import data
from app.schemas.clients import Client



class CLientsRepository:
    def __init__(self) -> None:
        self.data = data
        pass
    def get_clients(self):
        return data
    def get_client(self,client_id : int):
        return self.data
    pass