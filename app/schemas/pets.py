from pydantic import BaseModel
from typing import List


class Pets(BaseModel):
    id : int
    name : str
    race : str
    date : str

class ClientsSummary(BaseModel):
    couple_id : int
    client_id : int
    pet_id : int

    class Config:
        from_attributes = True

    
class PetsWithClients(BaseModel):
    id : int
    name : str
    race : str
    race : str
    date : str
    clients : List[ClientsSummary] = []

    class Config:
        from_attributes = True
        