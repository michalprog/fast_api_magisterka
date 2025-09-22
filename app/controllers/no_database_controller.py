from fastapi import APIRouter

router = APIRouter(prefix="/noDatabase", tags=["NoDatabase"])

@router.get("/")
def no_database_root():
    return {"message": "NoDatabase controller działa"}
