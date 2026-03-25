from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.repositories.database import get_db
from app.services.visits_services import VisitsServices
from app.schemas.visits import Visits,VisitsWithCompleteData

router = APIRouter(prefix= "/visits", tags= ["Visits"])
service = VisitsServices()


@router.get("/visits")
def get_visits(db: Session = Depends(get_db)):
    """
    Retrieves a list of all medical visits.
    """
    return service.get_visits(db)

@router.get("/visit/{visit_id}", response_model=VisitsWithCompleteData)
def get_visit(visit_id:int,db:Session = Depends(get_db)):
    """
    Retrieves a specific visit by ID, fully populated with client, pet, elements, and transactions.
    """
    return service.get_visit(db,visit_id)

@router.post("/new_visit")
def new_visit(visit:Visits,db:Session = Depends(get_db)):
    """
    Registers a new medical visit for a specific client-pet relationship.
    """
    return service.create_visit(db,visit) #type: ignore

@router.put("/update_visit/{visit_id}")
def update_visit(visit_id:int,visit:Visits,db:Session = Depends(get_db)):
    """
    Updates the details of an existing medical visit.
    """
    return service.update_visit(db,visit_id,visit) #type: ignore

@router.delete("/delete_visit/{visit_id}")
def delete_visit(visit_id:int,db:Session = Depends(get_db)):
    """
    Deletes a medical visit record.
    """
    return service.delete_visit(db,visit_id)

