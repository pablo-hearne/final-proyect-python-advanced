from fastapi import APIRouter
from app.schemas.clients import Client
# from app.services import ClientsServices

router = APIRouter(prefix= "clients", tags= ["Clients"])
# service = ClientsServices 


@router.get("/clients")
def get_clients():
    return None