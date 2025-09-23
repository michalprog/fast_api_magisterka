from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List, Dict
from app.repo.post_record_repository import PostRecordRepository
from app.config.database import SessionLocal

def get_all() -> List[PostRecordRepository]:
    with SessionLocal() as db:
        return db.query(PostRecordRepository).all()

def get_records(limit: int) -> List[PostRecordRepository]:
    with SessionLocal() as db:
        return db.query(PostRecordRepository).order_by(PostRecordRepository.id.asc()).limit(limit).all()

def create_records(records: List[Dict]) -> List[PostRecordRepository]:
    created = []
    with SessionLocal() as db:
        for record in records:
            new_record = PostRecordRepository(
                title=record["title"],
                description=record.get("description"),
                price=record["price"],
                active=record["active"],
            )
            db.add(new_record)
            created.append(new_record)
        db.commit()
        for r in created:
            db.refresh(r)
    return created

def update_records(records: List[Dict]) -> List[PostRecordRepository]:
    updated = []
    with SessionLocal() as db:
        for record in records:
            db_record = db.query(PostRecordRepository).filter(PostRecordRepository.id == record["id"]).first()
            if db_record:
                db_record.title = record.get("title", db_record.title)
                db_record.description = record.get("description", db_record.description)
                db_record.price = record.get("price", db_record.price)
                db_record.active = record.get("active", db_record.active)
                updated.append(db_record)
        db.commit()
        for r in updated:
            db.refresh(r)
    return updated

def delete_records(limit: int) -> int:
    with SessionLocal() as db:
        records_to_delete = (
            db.query(PostRecordRepository)
            .order_by(PostRecordRepository.id.asc())
            .limit(limit)
            .all()
        )
        count = len(records_to_delete)
        for r in records_to_delete:
            db.delete(r)
        db.commit()
    return count
