from sqlalchemy import Column, Integer, String, Table, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.repositories.database import Base

# Association table for many-to-many: elements <-> visits

Elements_used = Table(
    "Elements_used",
    Base.metadata,
    Column("elements_in_visit_id", Integer, autoincrement=True),
    Column("visit_id" , Integer , ForeignKey("visits.id") , primary_key=True),
    Column("element_id" , Integer , ForeignKey("elements.id") , primary_key=True)
)


class ElementsModel(Base):
    __tablename__ = "elements"

    id = Column(Integer, primary_key= True , index=True)
    name = Column(String , index=True)
    price = Column(Float, nullable = False)
    description = Column(String)

    visits = relationship("VisitsModel", secondary = Elements_used , back_populates = "elements")
