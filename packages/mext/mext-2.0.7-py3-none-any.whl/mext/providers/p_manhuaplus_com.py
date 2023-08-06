from mext.bases import MadaraBase


class ManhuaPlusCom(MadaraBase):

    def __init__(self, name, siteUrl):
        self.language = 'en'
        super(ManhuaPlusCom, self).__init__(name, siteUrl)
