from mext.bases import MangaStreamBase


class AsuraScansCom(MangaStreamBase):

    def __init__(self, name, siteUrl):
        self.language = 'en'
        super(AsuraScansCom, self).__init__(name, siteUrl)
