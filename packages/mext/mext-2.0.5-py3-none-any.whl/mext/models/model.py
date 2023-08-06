from typing import Dict


class Model:

    def __init__(self, provider):
        self.provider_name: str = provider.name

    @property
    def __dict__(self) -> Dict:
        return self.to_dict()

    def __iter__(self):
        for field in self.__slots__:
            yield (field, getattr(self, field))

    def __str__(self) -> str:
        return "{} {}".format(self.provider_name, self.__class__.__name__)

    def to_dict(self) -> Dict:
        return {field: getattr(self, field) for field in self.__slots__}
