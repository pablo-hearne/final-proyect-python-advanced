from pydantic import BaseModel
from typing import List





class Element(BaseModel):
    id : int
    name : str
    price : float
    description: str

class VisitsSummary(BaseModel):
    id : int
    client_and_pet_id : int
    date : str
    description : str
    total_cost : float

    class Config:
        from_attributes = True


class ElementWithVisits(BaseModel):
    id: int
    name : str
    price : float
    description : str
    visits : List[VisitsSummary] = []


    class Config:
        from_attributes = True



