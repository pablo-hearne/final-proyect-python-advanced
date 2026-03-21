from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.repositories.database import get_db
from app.services.elements_services import ElementsServices
from app.schemas.elements import Element,ElementWithVisits

router = APIRouter(prefix= "/elements", tags= ["Elements"])
service = ElementsServices()

@router.get("/elements")
def get_elements(db : Session = Depends(get_db)):
    return service.get_elements(db)

@router.get("/element/{element_id}",response_model=ElementWithVisits)
def get_element(element_id : int ,db : Session = Depends(get_db)):
    return service.get_element(db,element_id)

@router.post("/new_element")
def new_element(element:Element, db : Session = Depends(get_db)):
    return service.create_element(db,element)

@router.put("/update_element/{element_id}")
def update_element(element_id:int,element:Element,db : Session = Depends(get_db)):
    return service.update_element(db,element_id,element)

@router.delete("/delete_element/{element_id}")
def delete_element(element_id:int, db : Session = Depends(get_db)):
    return service.delete_element(db,element_id)
