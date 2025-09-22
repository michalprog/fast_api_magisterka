from fastapi import APIRouter

router = APIRouter(prefix="/postPerson", tags=["PostPerson"])

@router.get("/")
def post_person_root():
    return {"message": "PostPerson controller działa"}
