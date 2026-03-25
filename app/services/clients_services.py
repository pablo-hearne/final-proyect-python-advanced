from sqlalchemy.orm import Session

from app.repositories.models.clients_model import ClientsModel
from app.repositories.clients_repository import ClientsRepository


class ClientsServices:
    """
    Service layer for managing Client business logic.
    Acts as an intermediary between the controllers and the data repository.
    """
    def __init__(self):
        self.repository : ClientsRepository = ClientsRepository()

    def get_clients(self, db: Session):
        """
        Retrieves all clients.

        Args:
            db (Session): The database session.

        Returns:
            List[ClientsModel]: A list of all clients.
        """
        return self.repository.get_clients(db)
    
    def get_client(self, db:Session, client_id:int) -> ClientsModel:
        """
        Retrieves a specific client by ID.

        Args:
            db (Session): The database session.
            client_id (int): The ID of the client.

        Returns:
            ClientsModel: The requested client.
        """
        return self.repository.get_client(db,client_id)
    
    def create_client(self, db:Session, client:ClientsModel) -> ClientsModel:
        """
        Processes the creation of a new client.

        Args:
            db (Session): The database session.
            client (ClientsModel): The client data to save.

        Returns:
            ClientsModel: The created client.
        """
        return self.repository.create_client(db,client)
    
    def update_client(self, db:Session, client_id:int, client:ClientsModel) -> ClientsModel:
        """
        Processes the update of an existing client.

        Args:
            db (Session): The database session.
            client_id (int): The ID of the client to update.
            client (ClientsModel): The new client data.

        Returns:
            ClientsModel: The updated client.
        """
        return self.repository.update_client(db,client_id,client)
    
    def delete_client(self, db:Session, client_id:int)-> ClientsModel:
        """
        Processes the deletion of a client.

        Args:
            db (Session): The database session.
            client_id (int): The ID of the client to delete.

        Returns:
            Optional[ClientsModel]: The deleted client, or None if not found.
        """
        return self.repository.delete_client(db,client_id)



        


