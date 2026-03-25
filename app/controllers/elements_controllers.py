from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.repositories.database import get_db
from app.services.elements_services import ElementsServices
from app.schemas.elements import Element

router = APIRouter(prefix= "/elements", tags= ["Elements"])
service = ElementsServices()

@router.get("/elements")
def get_elements(db : Session = Depends(get_db)):
    """
    Retrieves the complete catalog of elements (services/supplies).
    """    
    return service.get_elements(db)

@router.get("/element/{element_id}",response_model=Element)
def get_element(element_id : int ,db : Session = Depends(get_db)):
    """
    Retrieves a specific element by ID.
    """
    return service.get_element(db,element_id)

@router.post("/new_element")
def new_element(element:Element, db : Session = Depends(get_db)):
    """
    Creates a new element in the catalog.
    """    
    return service.create_element(db,element) #type: ignore

@router.put("/update_element/{element_id}")
def update_element(element_id:int,element:Element,db : Session = Depends(get_db)):
    """
    Updates the details and pricing of an existing element.
    """
    return service.update_element(db,element_id,element) #type: ignore

@router.delete("/delete_element/{element_id}")
def delete_element(element_id:int, db : Session = Depends(get_db)):
    """
    Deletes an element from the catalog.
    """
    return service.delete_element(db,element_id)
