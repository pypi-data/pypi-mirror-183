import io

from .model import Model

class Cover(Model):
    """Represents a Cover."""
    __slots__ = (
        "id", "description", "volume", "file_bytes", "image_link", "url",
        "provider", "instance"
    )

    def __init__(self, provider):
        super().__init__(provider)

        self.id: str = ""
        self.description: str = ""
        self.volume: float = float(0)
        self.filename: str = ""
        self.file_bytes: io.BytesIO = io.BytesIO()
        self.image_link: str = ""
        self.url: str = ""
        self.provider = provider
        self.instance = self

    def __str__(self) -> str:
        return self.image_link

    def __repr__(self) -> str:
        return str(self)

    def get_url(self) -> str:
        return self.image_link or ""
