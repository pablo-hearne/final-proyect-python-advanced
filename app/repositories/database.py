# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# # URL de conexión a SQLite
# DATABASE_URL = "sqlite:///./test.db"

# # Crear motor de conexión a la base de datos
# engine = create_engine(
#     DATABASE_URL, connect_args={"check_same_thread": False}
# )

# # Crear una sesión para interactuar con la base de datos
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Base para definir los modelos de las tablas
# Base = declarative_base()



# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



"""Vamos a comparar los dos códigos para no perderme (uno con posgrade y otro con local)"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

import os

load_dotenv()

# URL de conexión de db de Render
DATABASE_URL = os.getenv("DATABASE_EXTERNAL_URL","sqlite:///./test.db")

# Crear motor de conexión a la base de datos
engine = create_engine(
    DATABASE_URL
)

# Crear una sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para definir los modelos de las tablas
Base = declarative_base()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
