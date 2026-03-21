from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.repositories.database import get_db
from app.services.pets_services import PetsServices
from app.schemas.pets import Pets,PetsWithClients

router = APIRouter(prefix= "/pets", tags= ["Pets"])
service = PetsServices()



@router.get("/pets")
def get_pets(db : Session = Depends(get_db)):
    return service.get_pets(db)

@router.get("/pet/{pet_id}",response_model=PetsWithClients)
def get_pet(pet_id:int, db: Session = Depends(get_db)):
    return service.get_pet(db,pet_id)

@router.post("/new_pet")
def create_pet(pet : Pets, db : Session = Depends(get_db)):
    return service.create_pet(db,pet)

@router.put("/update_pet/{pet_id}")
def update_pet(pet_id : int, pet:Pets, db: Session = Depends(get_db)):
    return service.update_pet(db,pet_id,pet)

@router.delete("/delete_pet/{pet_id}")
def delete_pet(pet_id : int, db: Session = Depends(get_db)):
    return service.delete_pet(db,pet_id)
