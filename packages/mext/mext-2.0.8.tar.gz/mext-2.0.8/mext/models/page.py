from .model import Model

class Page(Model):
    """Represents a Page"""
    __slots__ = (
        "id",
        "image_link",
        "provider", "instance"
    )

    def __init__(self, provider):
        super().__init__(provider)

        self.id: str = ""
        self.image_link: str = ""

    def __str__(self) -> str:
        return self.image_link

    def __repr__(self) -> str:
        return self.image_link
