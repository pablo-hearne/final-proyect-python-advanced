from pydantic import BaseModel
from typing import List



class Visits(BaseModel):
    """
    Scheme to register a new Visit.

    Attributes:
        client_and_pet_id (int): ID of the couple that came to the visit.
        date (str): Date of the visit.
        description (str): Diagnostic, treatment or other comments.
        total_cost (float): Total cost to charge.
    """
    client_and_pet_id : int
    date : str
    description : str
    total_cost : float


class ElementsSummary(BaseModel):
    """Elements Summary used in the visit"""
    id : int
    name : str
    price : float
    description : str

    class Config:
        from_attributes = True


class TransacationSummary(BaseModel):
    """Summary of the payments made in the visit."""
    id : int
    type_of_payment : str
    amount : float

    class Config:
        from_attributes = True

class ClientVisiting(BaseModel):
    """Visiting Client's information"""
    id : int
    name : str
    number : str
    email: str
    adress : str
    
    class Config:
        from_attributes = True


class PetVisiting(BaseModel):
    """Visiting patient's (Pet) information"""
    id : int
    name : str
    race : str
    date : str



class VisitsWithCompleteData(BaseModel):
    """
    Complete Visit response scheme. 

    Includes the nested information of the owner, the pet,
    the elements used and the transactions involved.

    Attributes:
        id (int): Visit ID.
        client_and_pet_id (int): Couple involved in the visit ID.
        date (str): Date of the visit.
        description (str): Visit details.
        total_cost (float): Total cost of the visit.
        elements (List[ElementsSummary]): List containing the Elements used.
        transactions (List[TransactionSummary]): List containing the transactions involved.
        client (ClientVisiting): Client's data.
        pet (PetVisiting): Pet's data.
    """
    id : int
    client_and_pet_id : int
    date : str
    description : str
    total_cost : float

    elements : List[ElementsSummary] = []
    transactions : List[TransacationSummary] = []
    client : ClientVisiting
    pet : PetVisiting
    