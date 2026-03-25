from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload

from app.repositories.models.transaction_model import TransactionsModel

class TransactionsRepository:
    """
    Repository class for managing Transaction database operations.
    """
    def get_transactions(self, db:Session) ->list[TransactionsModel]:
        """
        Retrieves all transactions from the database.

        Args:
            db (Session): The database session.

        Returns:
            List[TransactionsModel]: A list of all recorded transactions.
        """
        return db.query(TransactionsModel).all()
    
    def get_transaction(self, db:Session, transaction_id:int) ->TransactionsModel:
        """
        Retrieves a specific transaction and its associated visit by ID.

        Args:
            db (Session): The database session.
            transaction_id (int): The ID of the transaction to retrieve.

        Raises:
            HTTPException: If the transaction is not found (404).

        Returns:
            TransactionsModel: The requested transaction object.
        """
        transaction = db.query(TransactionsModel).options(
            joinedload(TransactionsModel.visit)
        ).filter_by(id=transaction_id).first()

        if not transaction:
            raise HTTPException(404,"Transaction not found")
        return transaction
    
    def create_transaction(self, db:Session, transaction:TransactionsModel) ->TransactionsModel:
        """
        Creates a new transaction linked to a specific visit.

        Args:
            db (Session): The database session.
            transaction (TransactionsModel): The transaction data to insert.

        Returns:
            TransactionsModel: The newly created transaction object.
        """
        new_transaction = TransactionsModel(
            visit_id = transaction.visit_id,
            type_of_payment = transaction.type_of_payment,
            amount = transaction.amount
        )
        db.add(new_transaction)
        db.commit()
        db.refresh(new_transaction)
        return new_transaction
    
    def update_transaction(self, db:Session, transaction_id:int, transaction:TransactionsModel) ->TransactionsModel:
        """
        Updates an existing transaction's information.

        Args:
            db (Session): The database session.
            transaction_id (int): The ID of the transaction to update.
            transaction (TransactionsModel): The new transaction data.

        Raises:
            HTTPException: If the transaction is not found (404).

        Returns:
            TransactionsModel: The updated transaction object.
        """
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
    
    def delete_transaction(self, db:Session, transaction_id:int) ->TransactionsModel:
        """
        Deletes a transaction from the database.

        Args:
            db (Session): The database session.
            transaction_id (int): The ID of the transaction to delete.

        Raises:
            HTTPException: If the transaction is not found (404).

        Returns:
            Optional[TransactionsModel]: The deleted transaction object.
        """
        db_transaction = db.query(TransactionsModel).filter_by(id=transaction_id).first()
        if not db_transaction:
            raise HTTPException(404,"Transaction not found")
        
        db.delete(db_transaction)
        db.commit()

        return db_transaction
    
