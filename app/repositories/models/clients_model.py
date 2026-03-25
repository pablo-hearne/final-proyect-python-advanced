from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.repositories.database import Base


class ClientsModel(Base):
    """
    Model for the Clients' Database.

    Represents the owners of the pets registered in-sistem.
    
    Attributes:
            id (int): Unique client identifier (Autoincremental).
            name (str): Complete name of the client.
            number (str): Clients' phone number.
            email (str): Clients' email.
            adress (str): Clients' Home adress.
    """
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String, index=True)
    number = Column(Integer)
    email = Column(String)
    adress = Column(String)

    pets_association = relationship("Client_and_pet", back_populates="client")

    @property
    def pets(self):
        """
        Obtains the list of pets associated to the client.

        Returns:
            list: List of objets "PetsModel" associated to the client.
        """
        return [assoc.pet for assoc in self.pets_association]