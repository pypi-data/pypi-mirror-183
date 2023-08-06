from .model import Model

class Person(Model):
    """Represents a Author or Artist or any related Person"""
    __slots__ = (
        "id", "name", "image_link", "bio", "url",
        "provider", "instance",
    )

    def __init__(self, provider):
        super().__init__(provider)
        
        self.id: str = ""
        self.name: str = ""
        self.image_link: str = ""
        self.bio: str = ""
        self.url: str = ""
        self.provider = provider
        self.instance = self

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return str(self)