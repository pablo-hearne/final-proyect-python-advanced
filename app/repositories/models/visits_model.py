from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.repositories.database import Base
from app.repositories.models.elements_model import Elements_used

class VisitsModel(Base):
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
        # Si existe el puente, devuelve el cliente. Si no, devuelve None.
        return self.couple.client if self.couple else None

    @property
    def pet(self):
        # Si existe el puente, devuelve la mascota. Si no, devuelve None.
        return self.couple.pet if self.couple else None


# comment n°1: 
# Es: La verdad es que a veces viene un cliente con varias mascotas, pero una cosa a la vez
# En: truth is, many times a client comes with more than just one pet, but i would like to treat the problems as they come (one at the time)
