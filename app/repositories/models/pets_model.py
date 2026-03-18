
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.repositories.database import Base
from app.repositories.models.clients_model import Client_and_pet

class PetsModel(Base):
    __tablename__ = "pets"

    id = Column(Integer,index=True,primary_key=True)
    name = Column(String,index=True)
    race = Column(String)
    date = Column(String)

    client = relationship("ClientsModel", secondary= Client_and_pet, back_populates="pets")