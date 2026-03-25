from pydantic import BaseModel


class Transactions(BaseModel):
    """
    Esquema para registrar un nuevo pago o transacción.

    Attributes:
        visit_id (int): ID de la visita médica a la que aplica el pago.
        type_of_payment (str): Método de pago (Efectivo, Tarjeta, etc.).
        amount (float): Monto a pagar.
    """
    visit_id : int
    type_of_payment : str
    amount : float


class VisitOfTransaction(BaseModel):
    """
    Resumen de la visita médica asociada a una transacción.

    Attributes:
        id (int): ID de la visita.
        client_and_pet_id (int): ID de la pareja (Dueño-Mascota).
        date (str): Fecha de la consulta.
        description (str): Motivo de la visita.
        total_cost (float): Costo total de la consulta.
    """
    id : int
    client_and_pet_id : int
    date : str
    description : str
    total_cost : float

    class Config:
        from_attributes = True

class TransactionsWithVisit(BaseModel):
    """
    Esquema de respuesta de una Transacción, incluyendo la visita que pagó.

    Attributes:
        visit_id (int): ID de la visita.
        type_of_payment (str): Método de pago utilizado.
        amount (float): Monto abonado.
        visit (VisitOfTransaction): Detalles de la visita médica pagada.
    """
    visit_id : int
    type_of_payment : str
    amount : float

    visit : VisitOfTransaction

