from sqlalchemy.orm import Session

from app.repositories.models.visits_model import VisitsModel
from app.repositories.visits_repository import VisitsRepository

class VisitsServices:
    def __init__(self) -> None:
        self.repository : VisitsRepository = VisitsRepository()
        pass

    def get_visits(self, db:Session):
        return self.repository.get_visits(db)
    
    def get_visit(self, db:Session, visit_id:int):
        return self.repository.get_visit(db,visit_id)
    
    def create_visit(self, db:Session, visit:VisitsModel):
        return self.repository.create_visit(db,visit)
    
    def update_visit(self, db:Session, visit_id:int, visit:VisitsModel):
        return self.repository.update_visit(db,visit_id,visit)
    
    def delete_visit(self, db:Session, visit_id:int):
        return self.repository.delete_visit(db,visit_id)
    
    
