from pydantic import BaseModel
from typing import Optional

class UniversalPerson(BaseModel):
    name: str
    surname: str
    salary: int
    role: int

class Statistics(BaseModel):
    role: str
    count: int
    averageSalary: float
    minSalaryPerson: UniversalPerson
    maxSalaryPerson: UniversalPerson
