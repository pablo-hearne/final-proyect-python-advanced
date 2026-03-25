from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.repositories.database import Base
from app.repositories.models.elements_model import Elements_used

class VisitsModel(Base):
    """
    Medical Visits' model for the database.

    Registers each visit linked to a specified couple (Client, Pet), 
    such as the elements used and the transactions related to the visit.

    Attributes:
        id (int): Unique identifier for the visit.
        client_and_pet_id (int): ID of the couple (Client-Pet) that asisted to the visit.
        date (str): Date of the visit.
        description (str): Motive or description of the visit.
        total_cost (float): Total cost of the visit, including the elements used.
    """
    __tablename__ = "visits"

    id = Column(Integer , nullable=False , autoincrement=True , primary_key=True , index=True)
    client_and_pet_id = Column(Integer , ForeignKey("client_and_pet.couple_id") , index=True)
    date = Column(String)
    description = Column(String)
    total_cost = Column(Float)

    elements = relationship("ElementsModel", secondary = Elements_used , back_populates= "visits" )
    transactions = relationship("TransactionsModel" , back_populates = "visit")
    couple = relationship("Client_and_pet", back_populates="visits")

    @property
    def client(self):
        """
        Function to obtain the client responsible for the visit.

        Returns:
            ClientsModel | None: Client object, or None if the bridge does not exist.
        """
        return self.couple.client if self.couple else None

    @property
    def pet(self):
        """
        Function to obtain the pet responsible for the visit.

        Returns:
            PetsModel | None: Pet object, or None if the bridge does not exist.
        """
        return self.couple.pet if self.couple else None


