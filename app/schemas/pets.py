from pydantic import BaseModel
from typing import List


class Pets(BaseModel):
    """
    Scheme o receive the data for creating a new pet.

    Attributes:
        name (str): Pet's name.
        race (str): Pet's race or species.
        date (str): Pet's Date of birth.
    """
    name : str
    race : str
    date : str

class ClientsSummary(BaseModel):
    """
    Scheme of summary of clients that own this pet.

    Attributes:
        id (int): Clients' ID.
        name (str): Complete name.
        number (str): Phone number.
        email (str): Email.
        adress (str): Home adress.
    """
    id : int
    name : str
    number : str
    email : str
    adress : str

    class Config:
        from_attributes = True

    
class PetsWithClients(BaseModel):
    """
    Scheme of the complete response of a pet, including owners.

    Attributes:
        id (int): Pet ID.
        name (str): Pet name.
        race (str): Pet's Race or species.
        date (str): Pet's Date of birth.
        clients (List[ClientsSummary]): Pet's owners list.
    """
    id : int
    name : str
    race : str
    race : str
    date : str
    clients : List[ClientsSummary] = []

    class Config:
        from_attributes = True
        