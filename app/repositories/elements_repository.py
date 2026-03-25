from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.models.elements_model import ElementsModel

class ElementsRepository:
    """
    Repository class for managing Element (Supplies/Services) database operations.
    """
    def get_elements(self, db:Session) -> list[ElementsModel]:
        """
        Retrieves all catalog elements from the database.

        Args:
            db (Session): The database session.

        Returns:
            List[ElementsModel]: A list of all available elements.
        """
        return db.query(ElementsModel).all()
    
    def get_element(self, db:Session, element_id:int):
        """
        Retrieves a specific element by ID.
        Note: The visits where the element was used are not included in this query.

        Args:
            db (Session): The database session.
            element_id (int): The ID of the element to retrieve.

        Raises:
            HTTPException: If the element is not found (404).

        Returns:
            ElementsModel: The requested element object.
        """
        element = db.query(ElementsModel).filter_by(id=element_id).first()
        # it really does not interest me to bring the visits they were used on, it's just the element
        if not element:
            raise HTTPException(404,"Element not found")
        return element
    
    def create_element(self, db:Session, element:ElementsModel):
        """
        Creates a new element in the catalog.

        Args:
            db (Session): The database session.
            element (ElementsModel): The element data to insert.

        Returns:
            ElementsModel: The newly created element object.
        """
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
        """
        Updates an existing element's information.

        Args:
            db (Session): The database session.
            element_id (int): The ID of the element to update.
            element (ElementsModel): The new element data.

        Raises:
            HTTPException: If the element is not found (404).

        Returns:
            ElementsModel: The updated element object.
        """
        db_element = db.query(ElementsModel).filter_by(id=element_id).first()
        if not db_element:
            raise HTTPException(404,"Element not found")
        db_element.name = element.name
        db_element.description = element.description
        db_element.price = element.price
        db.commit()
        db.refresh(db_element)
        return db_element

    def delete_element(self, db:Session, element_id:int):
        """
        Deletes an element from the database.

        Args:
            db (Session): The database session.
            element_id (int): The ID of the element to delete.

        Raises:
            HTTPException: If the element is not found (404).

        Returns:
            Optional[ElementsModel]: The deleted element object.
        """
        db_element = db.query(ElementsModel).filter_by(id=element_id).first()
        if not db_element:
            raise HTTPException(404,"Element not found")
        db.delete(db_element)
        db.commit()
        return db_element
