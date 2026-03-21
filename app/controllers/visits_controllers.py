from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.repositories.database import get_db
from app.services.visits_services import VisitsServices
from app.schemas.visits import Visits,VisitsWithCompleteData

router = APIRouter(prefix= "/visits", tags= ["Visits"])
service = VisitsServices()


@router.get("/visits")
def get_visits(db: Session = Depends(get_db)):
    return service.get_visits(db)

@router.get("/visit/{visit_id}", response_model=VisitsWithCompleteData)
def get_visit(visit_id:int,db:Session = Depends(get_db)):
    return service.get_visit(db,visit_id)

@router.post("/new_visit")
def new_visit(visit:Visits,db:Session = Depends(get_db)):
    return service.create_visit(db,visit)

@router.put("/update_visit/{visit_id}")
def update_visit(visit_id:int,visit:Visits,db:Session = Depends(get_db)):
    return service.update_visit(db,visit_id,visit)

@router.delete("/delete_visit/{visit_id}")
def delete_visit(visit_id:int,db:Session = Depends(get_db)):
    return service.delete_visit(db,visit_id)

