from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.repositories.database import Base
from app.repositories.models.clients_model import Client_and_pet
from app.repositories.models.elements_model import Elements_used

class VisitsModel(Base):
    __tablename__ = "visits"

    id = Column(Integer , nullable=False , autoincrement=True , primary_key=True , index=True)
    client_and_pet_id = Column(ForeignKey("Client_and_pet.couple_id") , index=True)
    date = Column(String)
    description = Column(String)
    total_cost = Column(Float)
    # transaction = Column(Integer , ForeignKey("transaction.id") , nullable = False)

    elements = relationship("ElementsModel", secondary = Elements_used , back_populates= "visits" )
    transactions = relationship("TransactionModel" , back_populates = "visit")
