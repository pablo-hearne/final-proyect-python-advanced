from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload


from app.repositories.models.clients_model import ClientsModel

class ClientsRepository:
    """
    Repository class for managing Client database operations.
    """

    def get_clients(self,db : Session) -> list[ClientsModel]:
        """
        Retrieves all clients from the database.

        Args:
            db (Session): The database session.

        Returns:
            List[ClientsModel]: A list of all registered clients.
        """
        return db.query(ClientsModel).all()
    

    def get_client(self,db : Session,client_id:int) -> ClientsModel:
        """
        Retrieves a specific client and their associated pets by ID.

        Args:
            db (Session): The database session.
            client_id (int): The ID of the client to retrieve.

        Raises:
            HTTPException: If the client is not found (404).

        Returns:
            ClientsModel: The requested client object.
        """
        client = db.query(ClientsModel).options(
            joinedload(ClientsModel.pets_association),
        ).filter_by(id=client_id).first()

        if not client:
            raise HTTPException(status_code=404, detail="Client not found")
        return client
    
    def create_client(self, db : Session, client:ClientsModel) ->ClientsModel:
        """
        Creates a new client in the database.

        Args:
            db (Session): The database session.
            client (ClientsModel): The client data to insert.

        Returns:
            ClientsModel: The newly created client object.
        """
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
    
    def update_client(self, db: Session, client_id : int, client : ClientsModel) -> ClientsModel:
        """
        Updates an existing client's information.

        Args:
            db (Session): The database session.
            client_id (int): The ID of the client to update.
            client (ClientsModel): The new client data.

        Raises:
            HTTPException: If the client is not found (404).

        Returns:
            ClientsModel: The updated client object.
        """
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
    
    def delete_client(self, db : Session , client_id : int) -> ClientsModel:
        """
        Deletes a client from the database.

        Args:
            db (Session): The database session.
            client_id (int): The ID of the client to delete.
        
        Raises:
            HTTPException: If the client is not found (404).

        Returns:
            ClientsModel: The deleted client object
        """
        db_client = db.query(ClientsModel).filter_by(id=client_id).first()
        if db_client:
            db.delete(db_client)
            db.commit()
            return db_client
        else:
            raise HTTPException(404, "Client not found")
    





