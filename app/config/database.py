from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app import app_consts

engine = create_engine(app_consts.DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency do wstrzykiwania sesji w endpointach
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
