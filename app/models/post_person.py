from typing import Optional
from pydantic import BaseModel

class PostPerson(BaseModel):
    id: Optional[int] = None
    name: str
    surname: str
    salary: int
    description: Optional[str] = None
    role: int
    active: bool
