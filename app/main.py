from fastapi import FastAPI
from app.controllers import clients_controllers,elements_controllers,pets_controllers,transactions_controllers,visits_controllers
from app.repositories.database import Base,engine
# creo mi instancia de FastAPI

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(router=clients_controllers.router, prefix=f"/api/v1")
app.include_router(router=elements_controllers, prefix=f"/api/v1")
app.include_router(router=pets_controllers, prefix=f"/api/v1")
app.include_router(router=transactions_controllers, prefix=f"/api/v1")
app.include_router(router=visits_controllers, prefix=f"/api/v1")
