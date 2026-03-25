from pydantic import BaseModel
from typing import List



class Client(BaseModel):
    """
    Clients' scheme for recieving a new one.

    Attributes:
        name (str): Complete name of the client.
        number (str): Phone number of the client.
        email (str): Clients' email.
        adress (str): Clients' home adress.
    """
    name : str
    number : str
    email: str
    adress : str

class PetsSummary(BaseModel):
    """
    Esquema de resumen de la mascota para mostrar dentro de un Cliente.
    Scheme for the summary of the clients' pets

    Attributes:
        id (int): Pets' ID.
        name (str): Pets name.
        race (str): Race or species.
        date (str): Date of birth of the pet.
    """
    id : int
    name : str
    race : str
    date : str

    class Config:
        from_attributes = True

class ClientWithPets(BaseModel):
    """
    Scheme of the complete answer of a Client, incling pets.

    Attributes:
        id (int): Client ID.
        name (str): Complete name.
        number (str): Client's Phone number.
        email (str):  Client's Email.
        adress (str): Client's Home Adress.
        pets (List[PetsSummary]): Client's pet List.
    """
    id : int
    name : str
    number : str
    email : str
    adress : str
    pets : List[PetsSummary] = []

    class Config:
        from_attributes = True 
