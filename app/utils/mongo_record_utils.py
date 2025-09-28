from typing import List, Dict


def get_records() -> List[Dict]:
    docs = list(mongo_record_collection.find())
    # zamieniamy ObjectId -> string
    for d in docs:
        d["id"] = str(d["_id"])
        d.pop("_id", None)
    return docs

def get_limited_records(limit: int) -> List[Dict]:
    docs = list(mongo_record_collection.find().limit(limit))
    records = []
    for d in docs:
        record = dict(d)
        record["id"] = str(record["_id"])
        record.pop("_id", None)
        records.append(record)
    return records

def create_records(records: List[Dict]) -> List[Dict]:
    # wstawiamy dokumenty (bez pola id)
    docs = [{k: v for k, v in r.items() if k != "id"} for r in records]
    result = mongo_record_collection.insert_many(docs)

    # uzupełniamy ID w rekordach
    for rec, inserted_id in zip(records, result.inserted_ids):
        rec["id"] = str(inserted_id)
    return records

from typing import List, Dict
from bson.objectid import ObjectId
from app.config.mongo_database import mongo_record_collection

def update_records(records: List[Dict]) -> List[Dict]:
    updated_records = []
    for record in records:
        record_id = record.get("id")
        if not record_id:
            continue

        try:
            object_id = ObjectId(record_id)
            data = {k: v for k, v in record.items() if k != "id"}

            # Update dokumentu
            result = mongo_record_collection.update_one(
                {"_id": object_id},
                {"$set": data}
            )

            # Jeśli dokument został znaleziony (niezależnie od tego, czy się zmienił)
            if result.matched_count > 0:
                fresh_doc = mongo_record_collection.find_one({"_id": object_id})
                if fresh_doc:
                    fresh_doc["id"] = str(fresh_doc["_id"])
                    fresh_doc.pop("_id", None)
                    updated_records.append(fresh_doc)

        except Exception as e:
            print(f" Błąd przy aktualizacji rekordu o id {record_id}: {e}")

    return updated_records


def delete_limited_records(limit: int) -> int:
    docs = list(mongo_record_collection.find().limit(limit))
    deleted_count = 0
    for d in docs:
        result = mongo_record_collection.delete_one({"_id": d["_id"]})
        if result.deleted_count > 0:
            deleted_count += 1
    return deleted_count
