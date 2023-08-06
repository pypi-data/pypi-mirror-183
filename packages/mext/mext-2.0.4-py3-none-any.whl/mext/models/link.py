from .model import Model

class Link(Model):
    """Represents a Link."""
    __slots__ = (
        "id", "name", "image_link", "link"
    )
    
    def __init__(self, provider):
        super().__init__(provider)

        self.id: str = ""
        self.name: str = ""
        self.image_link: str = ""
        self.link: str = ""
    
    def __str__(self) -> str:
        return f"{self.name} - {self.link}"
    
    def __repr__(self) -> str:
        return str(self)
    