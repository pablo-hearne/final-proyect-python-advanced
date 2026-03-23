from pydantic import BaseModel


class Transactions(BaseModel):
    visit_id : int
    type_of_payment : str
    amount : float


class VisitOfTransaction(BaseModel):
    id : int
    client_and_pet_id : int
    date : str
    description : str
    total_cost : float

    class Config:
        from_attributes = True

class TransactionsWithVisit(BaseModel):
    visit_id : int
    type_of_payment : str
    amount : float

    visit : VisitOfTransaction

