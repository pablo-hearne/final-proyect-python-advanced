from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select


from app.repositories.models.clients_model import ClientsModel,Client_and_pet
from app.repositories.models.pets_model import PetsModel
from app.repositories.models.visits_model import VisitsModel

class Visits():

    def get_visits(self, db:Session):
        return db.query(VisitsModel).all()
    
    def get_visit(self, db:Session, visit_id:int):
        visit = db.query(VisitsModel).options(
            joinedload(VisitsModel.elements),
            joinedload(VisitsModel.transactions)
        ).filter_by(id = visit_id).first()

        if not visit:
            raise HTTPException(404,"Visit not found")
        
        """
        Option n° 1: wanna know if it's wrong and WHY it is wrong
        """

        # patient_and_owner = Client_and_pet.select().filter_by(couple_id = visit.client_and_pet_id)

        # client = db.query(ClientsModel).filter_by(id = patient_and_owner.c[1]).first()
        # pet = db.query(PetsModel).filter_by(id = patient_and_owner.c[2]).first()

        """
        Option n° 2: same here but i googled it 
        """

        stmt = select(Client_and_pet).where(
            Client_and_pet.c.couple_id == visit.client_and_pet_id
        )

        patient_and_owner = db.connection().execute(stmt).first()

        if patient_and_owner != None:
            patient_and_owner = patient_and_owner.tuple()
            client = db.query(ClientsModel).filter_by(id = patient_and_owner(1)).first()
            pet = db.query(PetsModel).filter_by(id = patient_and_owner(2)).first()
            
            return visit,client,pet
        
        return visit
        
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




