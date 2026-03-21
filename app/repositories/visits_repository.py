from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload

from app.repositories.models.visits_model import VisitsModel
from app.repositories.models.pets_model import Client_and_pet

class VisitsRepository:

    def get_visits(self, db:Session):
        return db.query(VisitsModel).all()
    
    def get_visit(self, db:Session, visit_id:int):
        visit = db.query(VisitsModel).options(
            joinedload(VisitsModel.elements),
            joinedload(VisitsModel.transactions)
        ).filter_by(id = visit_id).first()

        if not visit:
            raise HTTPException(404,"Visit not found")
        
        couple = db.query(Client_and_pet).options(
            joinedload(Client_and_pet.client),
            joinedload(Client_and_pet.pet)
        )

        return visit,couple
        
    def create_visit(self, db:Session, visit:VisitsModel):
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


    def update_visit(self, db:Session, visit_id:int,visit:VisitsModel):
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
    

    def delete_visit(self, db:Session, visit_id:int):
        db_visit = db.query(VisitsModel).filter_by(id = visit_id).first()
        if not db_visit:
            raise HTTPException(404,"Visit not found")
        if db_visit:
            db.delete(db_visit)
            db.commit()
            return db_visit




