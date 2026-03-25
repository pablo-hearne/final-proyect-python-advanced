from pydantic import BaseModel





class Element(BaseModel):
    """
    Scheme for creating a new element (Object or Service)

    Attributes:
        name (str): Element's name .
        price (float): Element's price.
        description (str): Element's details.
    """
    name : str
    price : float
    description: str



class ElementWithVisits(BaseModel):
    """
    Response scheme for elements information.

    Attributes:
        id (int): Element's ID.
        name (str): Element's name.
        price (float): Element's price.
        description (str): Element's description.
    """
    id: int
    name : str
    price : float
    description : str


    class Config:
        from_attributes = True



