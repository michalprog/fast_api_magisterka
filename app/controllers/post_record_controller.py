from fastapi import APIRouter

router = APIRouter(prefix="/postRecord", tags=["PostRecord"])

@router.get("/")
def post_record_root():
    return {"message": "PostRecord controller działa"}
