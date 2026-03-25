from sqlalchemy.orm import Session


from app.repositories.models.transaction_model import TransactionsModel
from app.repositories.transactions_repository import TransactionsRepository


class TransactionsServices:
    """
    Service layer for managing Transaction business logic.
    """
    def __init__(self):
        self.repository : TransactionsRepository = TransactionsRepository()

    def get_transactions(self, db:Session)-> list[TransactionsModel]:
        """
        Service layer for managing Transaction business logic.
        """
        return self.repository.get_transactions(db)
    
    def get_transaction(self, db:Session, transaction_id:int)-> TransactionsModel:
        """
        Retrieves a specific transaction by ID.

        Args:
            db (Session): The database session.
            transaction_id (int): The ID of the transaction.

        Returns:
            TransactionsModel: The requested transaction.
        """
        return self.repository.get_transaction(db,transaction_id)
    
    def create_transaction(self, db:Session, transaction:TransactionsModel)-> TransactionsModel:
        """
        Processes the creation of a new transaction.

        Args:
            db (Session): The database session.
            transaction (TransactionsModel): The transaction data to save.

        Returns:
            TransactionsModel: The created transaction.
        """
        return self.repository.create_transaction(db,transaction)
    
    def update_transaction(self, db:Session, transaction_id:int, transaction:TransactionsModel)-> TransactionsModel:
        """
        Processes the update of an existing transaction.

        Args:
            db (Session): The database session.
            transaction_id (int): The ID of the transaction to update.
            transaction (TransactionsModel): The new transaction data.

        Returns:
            TransactionsModel: The updated transaction.
        """
        return self.repository.update_transaction(db,transaction_id,transaction)
    
    def delete_transaction(self, db:Session, transaction_id:int)-> TransactionsModel:
        """
        Processes the deletion of a transaction.

        Args:
            db (Session): The database session.
            transaction_id (int): The ID of the transaction to delete.
        
        Raises:
            HTTPException: if the transaction is not found (404)

        Returns:
            Optional[TransactionsModel]: The deleted transaction, or None if not found.
        """
        return self.repository.delete_transaction(db,transaction_id)
    
    
