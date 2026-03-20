from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload


from app.repositories.models.clients_model import ClientsModel,Client_and_pet

class ClientsRepository:


    def get_clients(self,db : Session):
        return db.query(ClientsModel).all()
    

    def get_client(self,db : Session,client_id:int):
        """
        returns the solicited client and the id of the pet(s) owned by said client
        """
        client = db.query(ClientsModel).options(
            joinedload(ClientsModel.pets),
        ).filter_by(id=client_id).first()
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")
        
        owned_pets = db.query(Client_and_pet).filter_by(client_id = client_id).all()

        return client,owned_pets
    
    def create_client(self, db : Session, client:ClientsModel):
        new_client = ClientsModel(
            name = client.name,
            adress = client.adress,
            number = client.number,
            email = client.email
        )
        db.add(new_client)
        db.commit()
        db.refresh(new_client)
        return new_client
    
    def update_client(self, db: Session, client_id : int, client : ClientsModel):
        db_client = db.query(ClientsModel).filter_by(id=client_id).first()
        if not db_client:
            raise HTTPException(status_code=404, detail="Client not found")
        if db_client:
            db_client.name = client.name
            db_client.adress = client.adress
            db_client.email = client.email
            db_client.number = client.number
        db.commit()
        db.refresh(db_client)
        return db_client
    
    def delete_client(self, db : Session , client_id : int):
        db_client = db.query(ClientsModel).filter_by(id=client_id).first()
        # db_client = db.query(ClientsModel).filter_by(ClientsModel.id == client_id).first()   # Cuál es la diferencia entre ambos?
        if db_client:
            db.delete(db_client)
            db.commit()
            return db_client
    





