from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.repositories.database import get_db
from app.services.transactions_services import TransactionsServices
from app.schemas.transactions import TransactionsWithVisit,Transactions

router = APIRouter(prefix= "/transactions", tags= ["Transactions"])
service = TransactionsServices()


@router.get("/transactions")
def get_transactions(db: Session = Depends(get_db)):
    return service.get_transactions(db)

@router.get("/transaction/{transaction_id}", response_model= TransactionsWithVisit)
def get_transaction(transaction_id:int,db:Session = Depends(get_db)):
    return service.get_transaction(db,transaction_id)

@router.post("/new_transaction")
def new_transaction(transaction : Transactions, db:Session = Depends(get_db)):
    return service.create_transaction(db,transaction)

@router.put("/update_transaction")
def update_transaction(transaction_id:int,transaction:Transactions,db:Session = Depends(get_db)):
    return service.update_transaction(db,transaction_id,transaction)

@router.delete("/delete_transaction/{transaction_id}")
def delete_transaction(transaction_id:int,db:Session = Depends(get_db)):
    return service.delete_transaction(db,transaction_id)
