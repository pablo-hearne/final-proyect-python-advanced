from fastapi import HTTPException
from sqlalchemy.orm import Session


from app.repositories.models.elements_model import ElementsModel

class ElementsRepository:
    def get_elements(self, db:Session):
        return db.query(ElementsModel).all()
    
    def get_element(self, db:Session, element_id:int):
        element = db.query(ElementsModel).filter_by(id=element_id).first()
        # it really does not interest me to bring the visits they were used on, it's just the element
        if not element:
            raise HTTPException(404,"Element not found")
        return element
    
    def create_element(self, db:Session, element:ElementsModel):
        new_element = ElementsModel(
            name = element.name,
            description = element.description,
            price = element.price,
        )
        db.add(new_element)
        db.commit()
        db.refresh(new_element)
        return new_element
    
    def update_element(self, db:Session, element_id:int, element:ElementsModel):
        db_element = db.query(ElementsModel).filter_by(id=element_id).first()
        if not db_element:
            raise HTTPException(404,"Element not found")
        if db_element: 
            db_element.name = element.name
            db_element.description = element.description
            db_element.price = element.price
        db.commit()
        db.refresh(db_element)
        return db_element

    def delete_element(self, db:Session, element_id:int):
        db_element = db.query(ElementsModel).filter_by(id=element_id).first()
        if not db_element:
            raise HTTPException(404,"Element not found")
        if db_element:
            db.delete(db_element)
            db.commit()
            return db_element
