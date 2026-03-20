from sqlalchemy.orm import Session


from app.repositories.models.transaction_model import TransactionsModel
from app.repositories.transactions_repository import TransactionsRepository


class TransactionsServices:
    def __init__(self):
        self.repository : TransactionsRepository = TransactionsRepository()

    def get_transactions(self, db:Session):
        return self.repository.get_transactions(db)
    
    def get_transaction(self, db:Session, transaction_id:int):
        return self.repository.get_transaction(db,transaction_id)
    
    def create_transaction(self, db:Session, transaction:TransactionsModel):
        return self.repository.create_transaction(db,transaction)
    
    def update_transaction(self, db:Session, transaction_id:int, transaction:TransactionsModel):
        return self.repository.update_transaction(db,transaction_id,transaction)
    
    def delete_transaction(self, db:Session, transaction_id:int):
        return self.repository.delete_transaction(db,transaction_id)
    
    
