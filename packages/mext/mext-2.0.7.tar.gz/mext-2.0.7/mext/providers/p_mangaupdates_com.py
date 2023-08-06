import re

from datetime import datetime
from urllib.parse import ParseResult, urlencode, urlparse, urlunparse

from bs4 import BeautifulSoup

from mext import enums, models
from mext.exceptions import *
from mext.provider import Provider


# API getting Status code 500
# class MangaUpdatesCom(Provider):

#     def __init__(self, name, siteUrl):
#         self.language = 'en'
#         super(MangaUpdatesCom, self).__init__(name, siteUrl)

#         self.api_url = "https://api.mangaupdates.com/v1"

#     def process_url(self, url):
#         super().process_url(url)

#     def get_id(self, url):
#         self.process_url(url)
#         return self.parsed_url.path.split('/')[2]

#     def get_manga(self, url, params) -> models.Manga:
#         id = self.get_id(url)

#         req = self.client.http.get(url, params=params)

#         if req.status_code == 200:
#             manga = models.Manga(self)

#             return manga
#         elif req.status_code == 404:
#             raise NoContentError(req)
#         else:
#             raise APIError(req)


class MangaUpdatesCom(Provider):

    def __init__(self, name, siteUrl):
        self.language = 'en'
        super(MangaUpdatesCom, self).__init__(name, siteUrl)

    def process_url(self, url):
        super().process_url(url)

    def get_id(self, url):
        self.process_url(url)
        return self.parsed_url.path.split('/')[2]

    def get_content(self, url, params):
        req = self.client.http.get(url, params=params)
        self.find_error(req)

        return BeautifulSoup(req.content, 'lxml')

    def get_manga(self, url, params) -> models.Manga:
        id = self.get_id(url)

        req = self.client.http.get(url, params=params)
        self.find_error(req)

        soup = BeautifulSoup(req.content, 'lxml')

        wrong_field_values = ['-', 'N/A']

        manga = models.Manga()

        contents = soup.findAll('div', {'class': 'sContent'})

        # Title
        manga.title = contents\
            .find('span', {'class': 'releasestitle tabletitle'})\
            .string.replace('\n', '')

        if not manga.title:
            raise Exception(f"Error getting series title {url}")

        # Description
        try:
            desc = contents[0].find('div', {'id': 'div_desc_more'}).contents
        except:
            desc = contents[0].contents
        description = [str(d).replace('\n', '') for d in desc]
        description = [
            d for d in description if d and not '<' in d and not '_' in d and not 'Raw' in d]
        desc = "\n\n".join(description)
        manga.description = (desc if desc.strip()
                             not in wrong_field_values else '') or ""

        # Alternative Names
        alts = [alt for alt in contents[3].contents if alt !=
                '\n' and alt != 'N/A']
        manga.alts = alts

        # Comic Type
        ctype = contents[1].text.replace('\n', '')
        manga.comic_type = ctype if ctype not in wrong_field_values else None

        # Genres
        _genre_list = [genre.find('u')
                       .text.replace('[Add]', '').strip()
                       for genre in contents[14].findAll('a')][:-1]

        genre_list = []

        for genre_attr in _genre_list:
            genre = models.Genre(self)
            genre.name = genre_attr
            genre_list.append(genre)

        manga.genres = genre_list

        # Authors
        _author_list = [author.find('u').text.replace('[Add]', '').strip() for author in contents[18].findAll('a') if author.find('u').text != 'Add'] or \
            [author.strip().replace('\xa0', '')[:author.rfind('[')-1]
             for author in contents[18].text.split(',') if author.strip() != 'N/A']

        author_list = []

        for author_attr in _author_list:
            author = models.Person(self)
            author.name = author_attr
            author_list.append(author)

        manga.authors = author_list

        # Artists
        _artist_list = [artist.find('u').text.replace('[Add]', '').strip() for artist in contents[19].findAll('a') if artist.find('u').text != 'Add'] or \
            [artist.strip().replace('\xa0', '')[:artist.rfind('[')-1]
             for artist in contents[19].text.split(',') if artist.strip() != 'N/A']

        artist_list = []

        for artist_attr in _artist_list:
            artist = models.Person(self)
            artist.name = artist_attr
            artist_list.append(artist)

        manga.artists = artist_list

        # Tags
        full_tags = self.get_content(
            "https://www.mangaupdates.com/ajax/show_categories.php?s=%d&type=1" % sid
        ).findAll('a')
        explicit_tags = ['sex', 'rape', 'murder',
                         'child abuse', 'drug', 'log in']
        _tag_list =

        # Year

        return manga
