from fastapi import APIRouter

router = APIRouter(prefix="/mongoPerson", tags=["MongoPerson"])

@router.get("/")
def mongo_person_root():
    return {"message": "MongoPerson controller działa"}
