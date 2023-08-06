from typing import List
from datetime import datetime

from mext import models

from .model import Model


class Chapter(Model):
    """Represents a Chapter."""
    __slots__ = (
        "id", "name", "number", "volume", "language", "special", "pages", "page_count",
        "manga", "group", "uploader", "url", "created_at", "updated_at",
        "provider", "instance"
    )

    def __init__(self, provider):
        super().__init__(provider)
        
        self.id: str = ""
        self.name: str = ""
        self.number: str = ""
        self.volume: float = float(0)
        self.language: str = ""
        self.special: bool = False
        self.oneshot: bool = False
        self.pages: List[models.Page] = ""
        self.page_count: int = int(0)
        self.manga: models.Manga = None
        self.group: models.Group = None
        self.uploader: str = None
        self.url: str = ""
        self.created_at: datetime = None
        self.updated_at: datetime = None
        self.provider = provider
        self.instance = self

    def __str__(self) -> str:
        srep = f"Chapter {self.number}"
        if self.name:
            srep = f"{srep} - {self.name}"
        return srep

    def __repr__(self) -> str:
        return str(self)
