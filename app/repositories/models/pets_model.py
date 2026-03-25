
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.repositories.database import Base


class Client_and_pet(Base):
    """
    Model for the intermediate table for Client-Pets relationship

    Manages the "many-to-many" relation between Clients and Pets,
    allowing the client to have many pets and viceversa. 

    Attributes:
        couple_id (int): Unique identifier for the couple.
        client_id (int): Foreign key related to the client.
        pet_id (int): Foreign key related to the pet.
    """
    __tablename__ = "client_and_pet"

    couple_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), index=True)
    pet_id = Column(Integer, ForeignKey("pets.id"), index=True)


    client = relationship("ClientsModel", back_populates="pets_association")
    pet = relationship("PetsModel", back_populates="clients_association")
    visits = relationship("VisitsModel", back_populates="couple")


class PetsModel(Base):
    """
    Pets' model for the database.

    Attributes:
        id (int): Unique identifier for the patient.
        name (str): Name of the pet.
        race (str): Race or species of the pet.
        date (str): Date of birth of the patient.
    """
    __tablename__ = "pets"

    id = Column(Integer, index=True, primary_key=True)
    name = Column(String, index=True)
    race = Column(String)
    date = Column(String)

    clients_association = relationship("Client_and_pet", back_populates="pet")

    @property
    def clients(self):
        return [assoc.client for assoc in self.clients_association]