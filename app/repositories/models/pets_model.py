
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.repositories.database import Base
# from app.repositories.models.clients_model import Client_and_pet



Client_and_pet = Table(
    "Client_and_pet",
    Base.metadata,
    Column("couple_id" , Integer , nullable=False , autoincrement=True , index=True),
    Column("client_id" , Integer , ForeignKey("clients.id") , primary_key=True ,index=True),
    Column("pet_id" , Integer , ForeignKey("pets.id") , primary_key=True, index=True)
)



class PetsModel(Base):
    __tablename__ = "pets"

    id = Column(Integer,index=True,primary_key=True)
    name = Column(String,index=True)
    race = Column(String)
    date = Column(String)

    clients = relationship("ClientsModel", secondary= Client_and_pet, back_populates="pets")

