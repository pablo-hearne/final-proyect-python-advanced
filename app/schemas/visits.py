from pydantic import BaseModel
from typing import List



class Visits(BaseModel):
    client_and_pet_id : int
    date : str
    description : str
    total_cost : float


class ElementsSummary(BaseModel):
    id : int
    name : str
    price : float
    description : str

    class Config:
        from_attributes = True


class TransacationSummary(BaseModel):
    id : int
    type_of_payment : str
    amount : float

    class Config:
        from_attributes = True

class ClientVisiting(BaseModel):
    id : int
    name : str
    number : str
    email: str
    adress : str
    
    class Config:
        from_attributes = True


class PetVisiting(BaseModel):
    id : int
    name : str
    race : str
    date : str



class VisitsWithCompleteData(BaseModel):
    id : int
    client_and_pet_id : int
    date : str
    description : str
    total_cost : float

    elements : List[ElementsSummary] = []
    transactions : List[TransacationSummary] = []
    client : ClientVisiting
    pet : PetVisiting
    