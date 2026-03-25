from sqlalchemy.orm import Session

from app.repositories.models.visits_model import VisitsModel
from app.repositories.visits_repository import VisitsRepository

class VisitsServices:
    """
    Service layer for managing Medical Visits business logic.
    """
    def __init__(self) -> None:
        self.repository : VisitsRepository = VisitsRepository()
        

    def get_visits(self, db:Session)-> list[VisitsModel]:
        """
        Retrieves all medical visits.

        Args:
            db (Session): The database session.

        Returns:
            List[VisitsModel]: A list of all visits.
        """
        return self.repository.get_visits(db)
    
    def get_visit(self, db:Session, visit_id:int)-> VisitsModel:
        """
        Retrieves a specific medical visit by ID, including its context.

        Args:
            db (Session): The database session.
            visit_id (int): The ID of the visit.

        Returns:
            VisitsModel: The requested visit.
        """
        return self.repository.get_visit(db,visit_id)
    
    def create_visit(self, db:Session, visit:VisitsModel)-> VisitsModel:
        """
        Processes the creation of a new medical visit.

        Args:
            db (Session): The database session.
            visit (VisitsModel): The visit data to save.

        Returns:
            VisitsModel: The created visit.
        """
        return self.repository.create_visit(db,visit)
    
    def update_visit(self, db:Session, visit_id:int, visit:VisitsModel)-> VisitsModel:
        """
        Processes the update of an existing medical visit.

        Args:
            db (Session): The database session.
            visit_id (int): The ID of the visit to update.
            visit (VisitsModel): The new visit data.

        Returns:
            VisitsModel: The updated visit.
        """
        return self.repository.update_visit(db,visit_id,visit)
    
    def delete_visit(self, db:Session, visit_id:int)-> VisitsModel:
        """
        Processes the deletion of a medical visit.

        Args:
            db (Session): The database session.
            visit_id (int): The ID of the visit to delete.

        Returns:
            VisitsModel: The deleted visit.
        """
        return self.repository.delete_visit(db,visit_id)
    
    
