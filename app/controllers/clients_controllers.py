from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.repositories.database import get_db
from app.services.clients_services import ClientsServices
from app.schemas.clients import Client,ClientWithPets


router = APIRouter(prefix= "/clients", tags= ["Clients"])
service = ClientsServices()



@router.get("/clients")
def get_clients(db : Session = Depends(get_db)):
    return service.get_clients(db)

@router.get("/client/{client_id}", response_model=ClientWithPets)
def get_client(client_id:int, db:Session = Depends(get_db)):
    return service.get_client(db,client_id)

@router.post("/new_client",response_model=Client)
def create_client(client:Client, db:Session = Depends(get_db)): #acá quiero poner client : Client, pero me dice 
    return service.create_client(db,client)              #que debería ser ClientsModel (aiura)

@router.put("/update_client/{client_id}")
def update_client(client_id:int, client:Client, db:Session = Depends(get_db)): 
    return service.update_client(db, client_id, client)

@router.delete("/delete_client/{client_id}")
def delete_client( client_id:int, db:Session = Depends(get_db)):
    return service.delete_client(db,client_id)



