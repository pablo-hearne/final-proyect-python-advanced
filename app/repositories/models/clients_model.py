# from pydantic import BaseModel


# class Client(BaseModel):
#     name : str
#     pets : list
#     number : int
#     email: str
#     residence : str



"""Vamos a comparar los dos códigos (con posgrade y con FastAPI solo)"""

from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.repositories.database import Base



# Association table for many-to-many: clients <-> pets

Client_and_pet = Table(
    "Client_and_pet",
    Base.metadata,
    Column("couple_id" , Integer , nullable=False , autoincrement=True , index=True),
    Column("client_id" , Integer , ForeignKey("client.id") , primary_key=True ,index=True),
    Column("pet_id" , Integer , ForeignKey("pet.id") , primary_key=True, index=True)
)


class ClientsModel(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key= True, index= True)
    name = Column(String, index = True)
    number = Column(String)
    email = Column(String)
    adress = Column(String)


    pets = relationship("PetsModel", secondary = Client_and_pet, back_populates = "client")

