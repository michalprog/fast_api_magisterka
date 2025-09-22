from typing import Optional

# Zwykła klasa DTO używana w logice aplikacji
class PostRecord:
    def __init__(
        self,
        id: Optional[int] = None,
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

    def __repr__(self):
        return (
            f"<PostRecord id={self.id}, title={self.title}, price={self.price}, "
            f"active={self.active}, description={self.description}>"
        )
