from typing import Optional

class PostPerson:
    def __init__(self, id: Optional[int] = None, name: str = "", surname: str = "", salary: int = 0,
                 description: Optional[str] = None, role: int = 0):
        self.id = id
        self.name = name
        self.surname = surname
        self.salary = salary
        self.description = description
        self.role = role

    def __repr__(self):
        return f"<PostPerson id={self.id}, name={self.name}, surname={self.surname}, salary={self.salary}, role={self.role}>"
