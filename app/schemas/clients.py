from pydantic import BaseModel
from typing import List



class Client(BaseModel):
    name : str
    number : int
    email: str
    adress : str

class PetsSummary(BaseModel):
    couple_id : int
    client_id : int
    pet_id : int

    class Config:
        from_attributes = True

class ClientWithPets(BaseModel):
    id : int
    name : str
    number : int
    email : str
    residence : str
    pets : List[PetsSummary] = []

    class Config:
        from_attributes = True 
