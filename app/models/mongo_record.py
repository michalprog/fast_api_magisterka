from typing import Optional

class MongoRecord:
    def __init__(
        self,
        id: Optional[str] = None,
        title: str = "",
        description: Optional[str] = None,
        price: float = 0.0,
        active: bool = True,
    ):
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.active = active

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "active": self.active,
        }

    @staticmethod
    def from_dict(data: dict) -> "MongoRecord":
        return MongoRecord(
            id=str(data.get("id")) if data.get("id") else None,
            title=data.get("title", ""),
            description=data.get("description"),
            price=float(data.get("price", 0.0)),
            active=bool(data.get("active", True)),
        )
