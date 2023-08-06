from urllib.error import HTTPError
from urllib.parse import urlparse
from typing import List, Dict

from mext import models, client, utils


class Provider:

    def __init__(self, name, siteUrl):
        self.name = name
        self.siteUrl = siteUrl
        self.language = ''

        self.client = client.Client('http')

    def __str__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return str(self)

    def process_url(self, url):
        self.parsed_url = urlparse(url)
        self.scheme = self.parsed_url.scheme
        self.netloc = self.parsed_url.netloc

    def get_latest(self, url: str, params: Dict = {}) -> List[models.Manga]:
        """Gets list of updated mangas."""
        raise NotImplementedError

    def get_manga(self, url: str, params: Dict = {}) -> models.Manga:
        """Gets a manga with a specific url."""
        raise NotImplementedError

    def get_manga_list(self, url: str, params: Dict = {}) -> List[models.Manga]:
        """Gets a list of Manga."""
        raise NotImplementedError

    def get_chapter(self, url: str, params: Dict = {}) -> models.Chapter:
        """Gets a chapter with a specific url."""
        raise NotImplementedError

    def get_manga_chapters(self, url: str, params: Dict = {}) -> List[models.Chapter]:
        """Gets chapters associated with a specific Manga."""
        raise NotImplementedError

    def get_cover(self, url: str) -> models.Cover:
        """Gets cover data associated with a specific Manga."""

    def find_error(self, url):
        if self.client.is_selenium:
            logs = self.client.selenium._driver.get_log('performance')
            status_code = utils.get_status(logs)
        else:
            status_code = self.client.http.status_code

        http_error_msg = ""

        if isinstance(status_code, int):
            if 400 <= status_code < 500:
                http_error_msg = (
                    f"{status_code} Client Error for url: {url}"
                )

            elif 500 <= status_code < 600:
                http_error_msg = (
                    f"{status_code} Server Error for url: {url}"
                )

        if http_error_msg:
            raise HTTPError(url=url, code=status_code,
                            msg=http_error_msg, hdrs=None, fp=None)
