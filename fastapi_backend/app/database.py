from sqlalchemy import create_all_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Estructura: postgresql://usuario:contraseña@host:puerto/nombre_bd
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:@localhost:5432/tu_base_de_datos"

engine = create_all_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependencia para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()