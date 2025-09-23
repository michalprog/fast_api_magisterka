from fastapi import APIRouter
from typing import List, Dict
from app.utils import post_record_utils
from app.repo.post_record_repository import PostRecordRepository

router = APIRouter(prefix="/postRecord", tags=["PostRecord"])

@router.get("/getRecords")
def get_records(body: Dict):
    limit = body.get("limit", 10)
    return post_record_utils.get_records(limit)

@router.post("/createRecords")
def create_records(records: List[Dict]):
    return post_record_utils.create_records(records)

@router.put("/updateRecords")
def update_records(records: List[Dict]):
    return post_record_utils.update_records(records)

@router.delete("/deleteRecords")
def delete_records(body: Dict):
    limit = body.get("limit", 10)
    return {"deleted": post_record_utils.delete_records(limit)}
