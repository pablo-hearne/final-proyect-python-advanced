from sqlalchemy.orm import Session


from app.repositories.models.pets_model import PetsModel
from app.repositories.pets_repository import PetsRepository

class PetsServices:
    def __init__(self) -> None:
        self.repository : PetsRepository = PetsRepository()
        pass

    def get_pets(self, db:Session):
        return self.repository.get_pets(db)
    
    def get_pet(self, db:Session, pet_id:int):
        return self.repository.get_pet(db,pet_id)
    
    def create_pet(self, db:Session, pet:PetsModel):
        return self.repository.create_pet(db, pet)
    
    def update_pet(self, db:Session, pet_id:int, pet:PetsModel):
        return self.repository.update_pet(db,pet_id,pet)
    
    def delete_pet(self, db:Session, pet_id:int):
        return self.repository.delete_pet(db,pet_id)
    
