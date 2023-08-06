import re

from datetime import datetime
from urllib.parse import ParseResult, urlencode, urlparse, urlunparse

from bs4 import BeautifulSoup

from mext import enums
from mext import models
from mext.provider import Provider


class MadaraBase(Provider):

    def __init__(self, name, siteUrl):
        self.name = name
        super(MadaraBase, self).__init__(name, siteUrl)

    def get_manga(self, url, params) -> models.Manga:
        return 
