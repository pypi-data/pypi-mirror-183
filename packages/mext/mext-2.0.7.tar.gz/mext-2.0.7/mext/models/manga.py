from typing import List, Dict
from datetime import datetime

from mext import models

from .model import Model


class Manga(Model):
    """Represents a Manga."""
    __slots__ = (
        "id", "title", "alts", "description", "links", "language", "comic_type", "status",
        "year", "rating", "followers", "genres", "tags", "authors", "artists", "current_cover",
        "all_covers", "banner_picture", "content_rating", "first_chapter", "last_chapter", "chapter_list",
        "url", "created_at", "updated_at", "provider", "instance"
    )

    def __init__(self, provider):
        super().__init__(provider)
        
        self.id: str = ""
        self.title: str = ""
        self.alts: List[str] = []
        self.description: str = ""
        self.links: Dict = []
        self.language: str = None
        self.comic_type: str = ""
        self.status: str = None
        self.year: int = datetime.now().year
        self.rating: float = float(0)
        self.followers: int = int(0)
        self.genres: List[models.Genre] = []
        self.tags: List[models.Tag] = []
        self.authors: List[models.Person] = []
        self.artists: List[models.Person] = []
        self.current_cover: models.Cover = None
        self.all_covers: List[models.Cover] = []
        self.banner_picture: str = ""
        self.content_rating: str = ""
        self.first_chapter: models.Chapter = None
        self.last_chapter: models.Chapter = None
        self.chapter_list: List[models.Chapter] = []
        self.url: str = ""
        self.created_at: datetime = None
        self.updated_at: datetime = None
        self.provider = provider
        self.instance = self

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return str(self)
