from fastapi import APIRouter

router = APIRouter(prefix="/mongoRecord", tags=["MongoRecord"])

@router.get("/")
def mongo_record_root():
    return {"message": "MongoRecord controller działa"}
