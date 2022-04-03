import json
from typing import Union, overload, Set

from .base import Parser
from ..objects import Page, Database


class MarkdownParser(Parser):
    ext = 'md'

    @overload
    def __init__(self, skipkeys=False, ensure_ascii=True, check_circular=True,
                 allow_nan=True, cls=None, indent=None, separators=None,
                 default=None, sort_keys=False, **kw):
        ...

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def parse(self, doc_info: Union[Page, Database], children=None):
        if isinstance(doc_info, Database):
            return parse_database(doc_info, children)
        elif isinstance(doc_info, Page):
            return parse_page(doc_info)
        else:
            raise NotImplementedError()


def parse_database(d: Database, children: Set[Page]):
    pass


def parse_page(p: Page):
    return json.dumps(p.to_dict(), indent=2, ensure_ascii=False)
