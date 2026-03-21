from pydantic import BaseModel
from typing import List


class Transactions(BaseModel):
    id : int
    visit_id : int
    type_of_payment : str
    amount : float

