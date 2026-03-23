from pydantic import BaseModel
from typing import List


class Pets(BaseModel):
    name : str
    race : str
    date : str

class ClientsSummary(BaseModel):
    id : int
    name : str
    number : str
    email : str
    adress : str

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
        