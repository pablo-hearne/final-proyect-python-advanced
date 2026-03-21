from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.repositories.database import Base


class ClientsModel(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String, index=True)
    number = Column(Integer)
    email = Column(String)
    adress = Column(String)

    pets_association = relationship("Client_and_pet", back_populates="client")

    @property
    def pets(self):
        return [assoc.pet for assoc in self.pets_association]