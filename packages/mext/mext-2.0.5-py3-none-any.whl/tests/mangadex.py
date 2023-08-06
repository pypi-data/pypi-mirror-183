from pprint import pprint

from mext import Mext

latest_url = 'https://mangadex.org/'
manga_url = 'https://mangadex.org/title/d1c0d3f9-f359-467c-8474-0b2ea8e06f3d/bocchi-sensei-teach-me-mangadex'
chapter_url = 'https://mangadex.org/chapter/e183d3f4-fde0-4288-a1ed-8547490f84b3'


class MangadexTest:

    def __init__(self) -> None:
        self.mext: Mext = Mext()

    def test_latest(self):
        pprint(self.mext.get_latest(latest_url))

    def test_manga(self):
        pprint(self.mext.get_manga(manga_url).to_dict())

    def test_chapter(self):
        pprint(self.mext.get_chapter(chapter_url).to_dict())

    def test_chapter_list(self):
        chapter_list = self.mext.get_manga_chapters(manga_url)
        for chapter in chapter_list:
            print(chapter.number, chapter.name)


if __name__ == '__main__':
    atest = MangadexTest()
    # atest.test_latest()
    atest.test_manga()
    atest.test_chapter()
    atest.test_chapter_list()
