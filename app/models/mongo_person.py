from typing import Optional

class MongoPerson:
    def __init__(
        self,
        id: Optional[str] = None,
        name: str = "",
        surname: str = "",
        salary: int = 0,
        description: Optional[str] = None,
        role: int = 0,
    ):
        self.id = id
        self.name = name
        self.surname = surname
        self.salary = salary
        self.description = description
        self.role = role

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "salary": self.salary,
            "description": self.description,
            "role": self.role,
        }

    @staticmethod
    def from_dict(data: dict) -> "MongoPerson":
        return MongoPerson(
            id=str(data.get("id")) if data.get("id") else None,
            name=data.get("name", ""),
            surname=data.get("surname", ""),
            salary=data.get("salary", 0),
            description=data.get("description"),
            role=data.get("role", 0),
        )
