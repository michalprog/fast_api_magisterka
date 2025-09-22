from fastapi import APIRouter
from typing import List
from app.models.post_person import PostPerson
from app.utils.no_database_utils import transform_persons

router = APIRouter(prefix="/noDatabase", tags=["NoDatabase"])

@router.get("/heatlh")
def health_check():
    return "OK"

@router.put("/transformPersons", response_model=List[PostPerson])
def transform_persons_endpoint(persons: List[PostPerson]):
    return transform_persons(persons)
