from sqlalchemy.orm import Session


from app.repositories.models.elements_model import ElementsModel
from app.repositories.elements_repository import ElementsRepository

class ElementsServices:
    """
    Service layer for managing Element (Supplies/Services) business logic.
    """
    def __init__(self) -> None:
        self.repository : ElementsRepository = ElementsRepository()


    def get_elements(self, db:Session)-> list[ElementsModel]:
        """
        Retrieves all elements from the catalog.

        Args:
            db (Session): The database session.

        Returns:
            List[ElementsModel]: A list of all elements.
        """
        return self.repository.get_elements(db)
    
    def get_element(self, db:Session, element_id:int)-> ElementsModel:
        """
        Retrieves a specific element by ID.

        Args:
            db (Session): The database session.
            element_id (int): The ID of the element.

        Returns:
            ElementsModel: The requested element.
        """
        return self.repository.get_element(db,element_id)
    
    def create_element(self, db:Session, element:ElementsModel)-> ElementsModel:
        """
        Processes the creation of a new element.

        Args:
            db (Session): The database session.
            element (ElementsModel): The element data to save.

        Returns:
            ElementsModel: The created element.
        """
        return self.repository.create_element(db,element)
    
    def update_element(self, db:Session, element_id:int, element:ElementsModel)-> ElementsModel:
        """
        Processes the update of an existing element.

        Args:
            db (Session): The database session.
            element_id (int): The ID of the element to update.
            element (ElementsModel): The new element data.

        Returns:
            ElementsModel: The updated element.
        """
        return self.repository.update_element(db,element_id,element)
    
    def delete_element(self, db:Session, element_id:int)-> ElementsModel:
        """
        Processes the deletion of an element.

        Args:
            db (Session): The database session.
            element_id (int): The ID of the element to delete.

        Raises:
            HTTPexception: if the element is not found (404)

        Returns:
            ElementsModel: The deleted element, or None if not found.
        """
        return self.repository.delete_element(db,element_id)
    

    
