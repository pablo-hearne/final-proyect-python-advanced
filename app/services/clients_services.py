from sqlalchemy.orm import Session

from app.repositories.models.clients_model import ClientsModel
from app.repositories.clients_repository import ClientsRepository


class ClientsServices:
    def __init__(self):
        self.repository : ClientsRepository = ClientsRepository()

    def get_clients(self, db: Session):
        return self.repository.get_clients(db)
    
    def get_client(self, db:Session, client_id:int):
        return self.repository.get_client(db,client_id)
    
    def create_client(self, db:Session, client:ClientsModel):
        return self.repository.create_client(db,client)
    
    def update_client(self, db:Session, client_id:int, client:ClientsModel):
        return self.repository.update_client(db,client_id,client)
    
    def delete_client(self, db:Session, client_id:int):
        return self.repository.delete_client(db,client_id)



        


