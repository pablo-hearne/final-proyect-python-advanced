from app.schemas.clients import Client
from app.repositories.clients_repository import CLientsRepository


class ClientsServices:
    def __init__(self):
        self.repository : CLientsRepository = CLientsRepository
        


