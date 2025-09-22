from sqlalchemy import Column, Integer, String
from app.config.database import Base

# Model ORM odwzorowujący tabelę "person"
class PostPersonRepository(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    salary = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
    role = Column(Integer, nullable=False)
