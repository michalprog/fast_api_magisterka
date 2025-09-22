from sqlalchemy import Column, Integer, String, Float, Boolean
from app.config.database import Base


class PostRecordRepository(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    active = Column(Boolean, nullable=False)
