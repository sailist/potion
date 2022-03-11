from .common import NotionObject


class Pagination(NotionObject):
    def __init__(self, **kwargs):
        super().__init__(None, kwargs=kwargs)

    @property
    def results(self) -> list:
        return self['results']

    @property
    def has_more(self) -> bool:
        return self['has_more']

    @property
    def type(self) -> str:
        return self['type']

    @property
    def object(self):
        return self['object']
