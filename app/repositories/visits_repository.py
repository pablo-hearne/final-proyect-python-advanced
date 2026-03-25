from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload

from app.repositories.models.visits_model import VisitsModel
from app.repositories.models.pets_model import Client_and_pet

class VisitsRepository:
    """
    Repository class for managing Medical Visits database operations.
    """

    def get_visits(self, db:Session) ->list[VisitsModel]:
        """
        Retrieves all medical visits from the database.

        Args:
            db (Session): The database session.

        Returns:
            List[VisitsModel]: A list of all recorded visits.
        """
        return db.query(VisitsModel).all()
    
    def get_visit(self, db:Session, visit_id:int) ->VisitsModel:
        """
        Retrieves a specific visit with its full context (elements, transactions, 
        client, and pet details) by ID.

        Args:
            db (Session): The database session.
            visit_id (int): The ID of the visit to retrieve.

        Raises:
            HTTPException: If the visit is not found (404).

        Returns:
            VisitsModel: The requested visit object fully populated.
        """
        visit = db.query(VisitsModel).options(
            joinedload(VisitsModel.elements),
            joinedload(VisitsModel.transactions),
            joinedload(VisitsModel.couple).joinedload(Client_and_pet.client),
            joinedload(VisitsModel.couple).joinedload(Client_and_pet.pet)
        ).filter_by(id = visit_id).first()

        if not visit:
            raise HTTPException(404,"Visit not found")
        

        return visit
        

        
    def create_visit(self, db:Session, visit:VisitsModel) ->VisitsModel:
        """
        Creates a new medical visit record.

        Args:
            db (Session): The database session.
            visit (VisitsModel): The visit data to insert.

        Returns:
            VisitsModel: The newly created visit object.
        """
        new_visit = VisitsModel(
            client_and_pet_id = visit.client_and_pet_id,
            description = visit.description,
            date = visit.date,
            total_cost = visit.total_cost
        )
        db.add(new_visit)
        db.commit()
        db.refresh(new_visit)
        return new_visit


    def update_visit(self, db:Session, visit_id:int,visit:VisitsModel) ->VisitsModel:
        """
        Updates an existing medical visit's information.

        Args:
            db (Session): The database session.
            visit_id (int): The ID of the visit to update.
            visit (VisitsModel): The new visit data.

        Raises:
            HTTPException: If the visit is not found (404).

        Returns:
            VisitsModel: The updated visit object.
        """
        db_visit = db.query(VisitsModel).filter_by(id = visit_id).first()
        if not db_visit:
            raise HTTPException(404,"Visit not found")
        if db_visit:
            db_visit.client_and_pet_id = visit.client_and_pet_id
            db_visit.description = visit.description
            db_visit.date = visit.date
            db_visit.total_cost = visit.total_cost
        db.commit()
        db.refresh(db_visit)
        return db_visit
    

    def delete_visit(self, db:Session, visit_id:int) ->VisitsModel:
        """
        Deletes a medical visit from the database.

        Args:
            db (Session): The database session.
            visit_id (int): The ID of the visit to delete.

        Raises:
            HTTPException: If the visit is not found (404).

        Returns:
            VisitsModel: The deleted visit object.
        """
        db_visit = db.query(VisitsModel).filter_by(id = visit_id).first()
        if not db_visit:
            raise HTTPException(404,"Visit not found")
        db.delete(db_visit)
        db.commit()
        return db_visit




