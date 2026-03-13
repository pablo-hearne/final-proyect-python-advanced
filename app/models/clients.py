from pydantic import BaseModel


class Client(BaseModel):
    name : str
    pets : list
    number : int
    email: str
    residence : str