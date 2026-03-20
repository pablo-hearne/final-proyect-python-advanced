from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload



from app.repositories.models.pets_model import PetsModel
from app.repositories.models.clients_model import Client_and_pet

class PetsRepository:

    def get_pets(self, db : Session):
        return db.query(PetsModel).all()
    
    def get_pet(self,db : Session, pet_id : int ):
        """
        Returns the solicited pet and the id of the owner(s) of said pet
        """
        pet = db.query(PetsModel).filter_by(id = pet_id).first()
        if not pet:
            raise HTTPException(status_code=404, detail="Pet not found")
        owners = db.query(Client_and_pet).filter_by(pet_id = pet_id).all()
        return pet,owners
    
    def create_pet(self, db:Session , pet : PetsModel):
        new_pet = PetsModel(
            pet_name = pet.name,
            pet_date = pet.date,
            pet_race = pet.race,
            pet_client = pet.client
        )
        db.add(new_pet)
        db.commit()
        db.refresh(new_pet)
        return new_pet
    
    def update_pet(self, db:Session , pet_id : int, pet : PetsModel):
        db_pet = db.query(PetsModel).filter_by(id = pet_id).first()
        if not db_pet:
            raise HTTPException(404,"Pet not found")
        
        db_pet.name = pet.name
        db_pet.date = pet.date
        db_pet.race = pet.race
        db.commit()
        db.refresh(db_pet)
        return db_pet
    
    def delete_pet(self, db:Session, pet_id:int):
        db_pet = db.query(PetsModel).filter_by(id=pet_id).first()

        db.delete(db_pet)
        db.commit()
        
        return db_pet