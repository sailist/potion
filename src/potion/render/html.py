import json
from typing import Union, overload

from .base import Parser
from ..objects import Page, Database


class HTMLParser(Parser):
    ext = 'html'

    @overload
    def __init__(self, skipkeys=False, ensure_ascii=True, check_circular=True,
                 allow_nan=True, cls=None, indent=None, separators=None,
                 default=None, sort_keys=False, **kw): ...

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def parse(self, doc_info: Union[Page, Database]):
        return json.dumps(doc_info.to_dict(), **self._config)


def parse_database(d: Database):
    pass


def parse_page(p: Page):
    pass
