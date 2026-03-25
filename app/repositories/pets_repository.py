from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload


from app.repositories.models.pets_model import PetsModel, Client_and_pet

class PetsRepository:
    """
    Repository class for managing Pet database operations.
    """

    def get_pets(self, db : Session) ->list[PetsModel]:
        """
        Retrieves all pets from the database.

        Args:
            db (Session): The database session.

        Returns:
            List[PetsModel]: A list of all registered pets.
        """
        return db.query(PetsModel).all()
    
    def get_pet(self,db : Session, pet_id : int ) ->PetsModel:
        """
        Retrieves a specific pet and its associated owners by ID.

        Args:
            db (Session): The database session.
            pet_id (int): The ID of the pet to retrieve.

        Raises:
            HTTPException: If the pet is not found (404).

        Returns:
            PetsModel: The requested pet object.
        """
        pet = db.query(PetsModel).options(
            joinedload(PetsModel.clients_association)
        ).filter_by(id = pet_id).first()
        if not pet:
            raise HTTPException(status_code=404, detail="Pet not found")
        return pet
    
    def create_pet(self, db:Session , pet : PetsModel, client_id:int) ->PetsModel:
        """
        Creates a new pet and automatically associates it with an existing client.

        Args:
            db (Session): The database session.
            pet (PetsModel): The pet data to insert.
            client_id (int): The ID of the owner (client).

        Returns:
            PetsModel: The newly created pet object.
        """
        new_pet = PetsModel(
            name = pet.name,
            date = pet.date,
            race = pet.race,
        )
        db.add(new_pet)
        db.flush()
        new_association = Client_and_pet(
            client_id = client_id,
            pet_id = new_pet.id
        )
        db.add(new_association)
        db.commit()
        db.refresh(new_pet)
        return new_pet
    
    def update_pet(self, db:Session , pet_id : int, pet : PetsModel) ->PetsModel:
        """
        Updates an existing pet's information.

        Args:
            db (Session): The database session.
            pet_id (int): The ID of the pet to update.
            pet (PetsModel): The new pet data.

        Raises:
            HTTPException: If the pet is not found (404).

        Returns:
            PetsModel: The updated pet object.
        """
        db_pet = db.query(PetsModel).filter_by(id = pet_id).first()
        if not db_pet:
            raise HTTPException(404,"Pet not found")
        
        db_pet.name = pet.name
        db_pet.date = pet.date
        db_pet.race = pet.race
        db.commit()
        db.refresh(db_pet)
        return db_pet
    
    def delete_pet(self, db:Session, pet_id:int) -> PetsModel:
        """
        Deletes a pet from the database.

        Args:
            db (Session): The database session.
            pet_id (int): The ID of the pet to delete.

        Raises:
            HTTPException: If the pet is not found (404).

        Returns:
            PetsModel: The deleted pet object.
        """
        db_pet = db.query(PetsModel).filter_by(id=pet_id).first()
        if not db_pet:
            raise HTTPException(404,"Pet not found")

        db.delete(db_pet)
        db.commit()
        return db_pet
    
        
    
    def associate_pet_with_client(self, db: Session, client_id: int, pet_id: int):
        """
        Creates a new association linking an existing pet to an additional owner.

        Args:
            db (Session): The database session.
            client_id (int): The ID of the new owner.
            pet_id (int): The ID of the pet.

        Returns:
            Dict[str, Any]: A dictionary containing a success message and the IDs.
        """
        new_association = Client_and_pet(
            client_id = client_id,
            pet_id = pet_id
        )
        db.add(new_association)
        db.commit()
        db.refresh(new_association)
        return {"message": f"Mascota vinculada al cliente {client_id} exitosamente","client_id":client_id,"pet_id":pet_id}