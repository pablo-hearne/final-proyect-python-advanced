from typing import List, Dict, Any
from sqlalchemy.orm import Session


from app.repositories.models.pets_model import PetsModel
from app.repositories.pets_repository import PetsRepository

class PetsServices:
    """
    Service layer for managing Pet business logic.
    """
    def __init__(self) -> None:
        self.repository : PetsRepository = PetsRepository()

    def get_pets(self, db:Session)-> list[PetsModel]:
        """
        Retrieves all pets.

        Args:
            db (Session): The database session.

        Returns:
            List[PetsModel]: A list of all pets.
        """
        return self.repository.get_pets(db)
    
    def get_pet(self, db:Session, pet_id:int)-> PetsModel:
        """
        Retrieves a specific pet by ID.

        Args:
            db (Session): The database session.
            pet_id (int): The ID of the pet.

        Returns:
            PetsModel: The requested pet.
        """
        return self.repository.get_pet(db,pet_id)
    
    def create_pet(self, db:Session, pet:PetsModel, client_id:int)-> PetsModel:
        """
        Processes the creation of a new pet and its association with an owner.

        Args:
            db (Session): The database session.
            pet (PetsModel): The pet data to save.
            client_id (int): The ID of the owner.

        Returns:
            PetsModel: The created pet.
        """
        return self.repository.create_pet(db, pet, client_id)
    
    def associate_pet_with_client(self, db:Session, client_id:int, pet_id:int)-> Dict[str,Any]:
        """
        Links an existing pet to an additional owner.

        Args:
            db (Session): The database session.
            client_id (int): The ID of the new owner.
            pet_id (int): The ID of the pet.

        Returns:
            Dict[str, Any]: A success message with the IDs.
        """
        return self.repository.associate_pet_with_client(db,client_id,pet_id)
    
    def update_pet(self, db:Session, pet_id:int, pet:PetsModel)-> PetsModel:
        """
        Processes the update of an existing pet.

        Args:
            db (Session): The database session.
            pet_id (int): The ID of the pet to update.
            pet (PetsModel): The new pet data.

        Returns:
            PetsModel: The updated pet.
        """
        return self.repository.update_pet(db,pet_id,pet)
    
    def delete_pet(self, db:Session, pet_id:int)-> PetsModel:
        """
        Processes the deletion of a pet.

        Args:
            db (Session): The database session.
            pet_id (int): The ID of the pet to delete.
        
        Raises:
            HTTPexception: if the pet is not found (404)

        Returns:
            PetsModel: The deleted pet
        """
        return self.repository.delete_pet(db,pet_id)
    
