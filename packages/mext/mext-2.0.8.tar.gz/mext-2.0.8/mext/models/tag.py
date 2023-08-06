from .model import Model

class Tag(Model):
    """Represents a Manga Tag."""
    __slots__ = (
        "id", "name", "description", "url",
        "provider", "instance"
    )

    def __init__(self, provider):
        super().__init__(provider)

        self.id: str = ""
        self.name: str = ""
        self.description: str = ""
        self.url: str = ""
        self.provider = provider
        self.instance = self

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return str(self)
