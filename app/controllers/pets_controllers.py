from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.repositories.database import get_db
from app.services.pets_services import PetsServices
from app.schemas.pets import Pets,PetsWithClients

router = APIRouter(prefix= "/pets", tags= ["Pets"])
service = PetsServices()



@router.get("/pets")
def get_pets(db : Session = Depends(get_db)):
    """
    Retrieves a list of all registered pets.
    """
    return service.get_pets(db)

@router.get("/pet/{pet_id}",response_model=PetsWithClients)
def get_pet(pet_id:int, db: Session = Depends(get_db)):
    """
    Retrieves a specific pet by ID, including its owners.
    """
    return service.get_pet(db,pet_id)

@router.post("/new_pet")
def create_pet(pet : Pets,client_id:int, db : Session = Depends(get_db)):
    """
    Registers a new pet and links it to an initial owner (client).
    """
    return service.create_pet(db,pet,client_id) #type: ignore

@router.post("/add_owner/{pet_id}/{client_id}")
def associate_pet_with_client(client_id: int, pet_id: int, db: Session= Depends(get_db)):
    """
    Links an existing pet to an additional owner.
    """
    return service.associate_pet_with_client(db,client_id,pet_id)

@router.put("/update_pet/{pet_id}")
def update_pet(pet_id : int, pet:Pets, db: Session = Depends(get_db)):
    """
    Updates the information of an existing pet.
    """
    return service.update_pet(db,pet_id,pet) #type: ignore

@router.delete("/delete_pet/{pet_id}")
def delete_pet(pet_id : int, db: Session = Depends(get_db)):
    """
    Deletes a pet from the database.
    """
    return service.delete_pet(db,pet_id)
