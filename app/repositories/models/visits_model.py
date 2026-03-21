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
    transactions = relationship("TransactionModel" , back_populates = "visit")


# comment n°1: 
# Es: La verdad es que a veces viene un cliente con varias mascotas, pero una cosa a la vez
# En: truth is, many times a client comes with more than just one pet, but i would like to treat the problems as they come (one at the time)
