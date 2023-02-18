from typing import List

from .common import NotionObject


class Pagination(NotionObject):
    def __init__(self, **kwargs):
        super().__init__(None, kwargs=kwargs)

    @property
    def results(self) -> List[NotionObject]:
        from potion.utils.parser import parse
        return [parse(i) for i in self['results']]

    @property
    def next_cursor(self):
        return self['next_cursor']

    @property
    def has_more(self) -> bool:
        return self['has_more']

    @property
    def type(self) -> str:
        return self['type']

    @property
    def object(self):
        return self['object']
