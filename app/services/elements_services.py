from sqlalchemy.orm import Session


from app.repositories.models.elements_model import ElementsModel
from app.repositories.elements_repository import ElementsRepository

class ElementsServices:
    def __init__(self) -> None:
        self.repository : ElementsRepository = ElementsRepository()
        pass

    def get_elements(self, db:Session):
        return self.repository.get_elements(db)
    
    def get_element(self, db:Session, element_id:int):
        return self.repository.get_element(db,element_id)
    
    def create_element(self, db:Session, element:ElementsModel):
        return self.repository.create_element(db,element)
    
    def update_element(self, db:Session, element_id:int, element:ElementsModel):
        return self.repository.update_element(db,element_id,element)
    
    def delete_element(self, db:Session, element_id:int):
        return self.repository.delete_element(db,element_id)
    

    
