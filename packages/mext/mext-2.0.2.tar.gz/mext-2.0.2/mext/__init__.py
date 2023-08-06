from urllib.parse import urlparse
from typing import List

from mext import models, providers
from mext.provider import Provider


class Mext:

    def __init__(self) -> None:
        self.provider: Provider = None

    def set_provider(self, url):
        parsed_url = urlparse(url)

        provider_instance = providers.get_provider_instance(
            netloc=parsed_url.netloc
        )

        self.provider = provider_instance

    def get_provider(self, url: str) -> Provider:
        if not self.provider:
            self.set_provider(url)

        return self.provider

    def get_latest(self, url: str, page=1) -> List[models.Manga]:
        return self.get_provider(url).get_latest(url, page)

    def get_manga(self, url: str, page=1) -> models.Manga:
        return self.get_provider(url).get_manga(url, page)

    def get_manga_list(self, url: str, page=1) -> List[models.Manga]:
        return self.get_provider(url).get_manga_list(url, page)

    def get_chapter(self, url: str, page=1) -> models.Chapter:
        return self.get_provider(url).get_chapter(url, page)

    def get_manga_chapters(self, url: str, page=1) -> List[models.Chapter]:
        return self.get_provider(url).get_manga_chapters(url, page)

    @property
    def all_providers(self):
        return providers.providers_json
