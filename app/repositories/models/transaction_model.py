from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.repositories.database import Base



class TransactionsModel(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key = True, index = True)
    visit_id = Column(Integer, ForeignKey("visit.id") , nullable = False)
    type_of_payment = Column(String)
    amount = Column(Float)

    visit = relationship("VisitsModel" , back_populates = "transactions")
