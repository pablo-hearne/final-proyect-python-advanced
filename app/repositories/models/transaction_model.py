from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.repositories.database import Base



class TransactionsModel(Base):
    """
    Model of Financial Transactions for the database.

    Stores all payments realized. Linking the client and the visit involved in said transaction.

    Attributes:
        id (int): Unique transaction identifier.
        visit_id (int): Foreign Key related to the visit (or part of the visit) being paid.
        type_of_payment (str): Payment Method (Ej. Cash, Card, Transference).
        amount (float): Amount paid.
    """
    __tablename__ = "transactions"

    id = Column(Integer, primary_key = True, index = True)
    visit_id = Column(Integer, ForeignKey("visits.id") , nullable = False)
    type_of_payment = Column(String)
    amount = Column(Float)

    visit = relationship("VisitsModel" , back_populates = "transactions")


