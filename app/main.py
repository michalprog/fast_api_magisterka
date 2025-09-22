from fastapi import FastAPI
from app.config.database import Base, engine
from app.controllers import (
    no_database_controller,
    post_record_controller,
    mongo_record_controller,
    mongo_person_controller,
    post_person_controller,
)

app = FastAPI(title="FastAPI Magisterka")

# Rejestracja routerów
app.include_router(no_database_controller.router)
app.include_router(post_record_controller.router)
app.include_router(mongo_record_controller.router)
app.include_router(mongo_person_controller.router)
app.include_router(post_person_controller.router)
Base.metadata.create_all(bind=engine)
