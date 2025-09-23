from fastapi import APIRouter
from typing import List, Dict
from app.utils import mongo_record_utils

router = APIRouter(prefix="/mongoRecord", tags=["MongoRecord"])

@router.get("/getRecords")
def get_records(body: Dict):
    limit = body.get("limit")
    if limit:
        return mongo_record_utils.get_limited_records(limit)
    return mongo_record_utils.get_records()

@router.post("/createRecords")
def create_records(records: List[Dict]):
    return mongo_record_utils.create_records(records)

@router.put("/updateRecords")
def update_records(records: List[Dict]):
    return mongo_record_utils.update_records(records)

@router.delete("/deleteRecords")
def delete_records(body: Dict):
    limit = body.get("limit", 10)
    return {"deleted": mongo_record_utils.delete_limited_records(limit)}
