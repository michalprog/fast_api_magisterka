from fastapi import APIRouter
from typing import List, Dict
from app.utils import mongo_person_utils
from app.models.statistics import Statistics

router = APIRouter(prefix="/mongoPerson", tags=["MongoPerson"])

@router.get("/getAll")
def get_all_persons():
    return mongo_person_utils.get_all()

@router.post("/createPersons")
def create_persons(persons: List[Dict]):
    return mongo_person_utils.create_persons(persons)

@router.get("/personStatistics", response_model=List[Statistics])
def person_statistics():
    return mongo_person_utils.person_statistics()
