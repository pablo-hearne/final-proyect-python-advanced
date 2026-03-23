from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload

from app.repositories.models.transaction_model import TransactionsModel

class TransactionsRepository:
    def get_transactions(self, db:Session):
        return db.query(TransactionsModel).all()
    
    def get_transaction(self, db:Session, transaction_id:int):
        transaction = db.query(TransactionsModel).options(
            joinedload(TransactionsModel.visit)
        ).filter_by(id=transaction_id).first()

        if not transaction:
            raise HTTPException(404,"Transaction not found")
        return transaction
    
    def create_transaction(self, db:Session, transaction:TransactionsModel):
        new_transaction = TransactionsModel(
            visit_id = transaction.visit_id,
            type_of_payment = transaction.type_of_payment,
            amount = transaction.amount
        )
        db.add(new_transaction)
        db.commit()
        db.refresh(new_transaction)
        return new_transaction
    
    def update_transaction(self, db:Session, transaction_id:int, transaction:TransactionsModel):
        db_transaction = db.query(TransactionsModel).filter_by(id=transaction_id).first()
        if not db_transaction:
            raise HTTPException(404,"Transaction not found")
        if db_transaction:
            db_transaction.type_of_payment = transaction.type_of_payment, # type: ignore
            db_transaction.amount = transaction.amount
            db_transaction.visit_id = transaction.visit_id
            db.commit()
            db.refresh(db_transaction)
            
        return db_transaction
    
    def delete_transaction(self, db:Session, transaction_id:int):
        db_transaction = db.query(TransactionsModel).filter_by(id=transaction_id).first()
        if not db_transaction:
            raise HTTPException(404,"Transaction not found")
        if db_transaction:
            db.delete(db_transaction)
            db.commit()
        return db_transaction
    
