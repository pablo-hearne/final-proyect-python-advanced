from fastapi import FastAPI
from app.controllers import clients_controllers,elements_controllers,pets_controllers,transactions_controllers,visits_controllers
from app.repositories.database import Base,engine
from fastapi.middleware.cors import CORSMiddleware
# creo mi instancia de FastAPI

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["https://v0-veterinary-clinic-dashboard-two.vercel.app/"],
    allow_credentials= True,
    allow_methods = ["*"],
    allow_headers = ["*"]
    )

app.include_router(router=clients_controllers.router, prefix=f"/api/v1")
app.include_router(router=pets_controllers.router, prefix=f"/api/v1")
app.include_router(router=elements_controllers.router, prefix=f"/api/v1")
app.include_router(router=transactions_controllers.router, prefix=f"/api/v1")
app.include_router(router=visits_controllers.router, prefix=f"/api/v1")
