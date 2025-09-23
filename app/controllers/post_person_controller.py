from fastapi import APIRouter
from typing import List, Dict
from app.utils import post_person_utils
from app.models.statistics import Statistics

router = APIRouter(prefix="/postPerson", tags=["PostPerson"])

@router.get("/getAll")
def get_all_persons():
    return post_person_utils.get_all()

@router.post("/createPersons")
def create_persons(persons: List[Dict]):
    return post_person_utils.create_persons(persons)

@router.put("/personStatistics", response_model=List[Statistics])
def person_statistics():
    return post_person_utils.person_statistics()
