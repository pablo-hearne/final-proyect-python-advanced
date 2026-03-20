from app.schemas.clients import Client
from app.repositories.clients_repository import ClientsRepository


class ClientsServices:
    def __init__(self):
        self.repository : ClientsRepository = ClientsRepository # type: ignore

        


