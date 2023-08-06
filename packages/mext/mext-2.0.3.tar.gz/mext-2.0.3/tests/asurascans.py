from pprint import pprint

from mext import Mext

latest_url = 'https://asurascans.com/'
manga_url = 'https://asurascans.com/manga/rise-from-the-rubble/'
chapter_url = 'https://asurascans.com/rise-from-the-rubble-chapter-138/'


class AsuraScansTest:

    def __init__(self) -> None:
        self.mext = Mext()

    def test_latest(self):
        pprint(self.mext.get_latest(latest_url))

    def test_manga(self):
        pprint(self.mext.get_manga(manga_url))

    def test_manga_list(self):
        pprint(self.mext.get_manga_list(latest_url))

    def test_chapter(self):
        pprint(self.mext.get_chapter(chapter_url).to_dict())

    def test_chapter_list(self):
        chapter_list = self.mext.get_manga_chapters(manga_url)
        for chapter in chapter_list:
            print(chapter.number, chapter.name)


if __name__ == '__main__':
    atest = AsuraScansTest()
    atest.test_latest()
    atest.test_manga()
    atest.test_chapter()
    atest.test_chapter_list()
