import os
from collections import defaultdict
from typing import TYPE_CHECKING, List

from potion import Request
from potion.api import *
from potion.objects import Parent, Page, Properties, Database, sche
from potion.objects import prop, Error as NotionError
from .base import NotionObject

if TYPE_CHECKING:
    from .page import NotionPage


class NotionDatabase(NotionObject):
    def __init__(self, auth=None, id=None, parent: Parent = None):
        super().__init__(auth, id, parent)
        if auth is None:
            auth = os.environ.get('NOTION_SECRET', None)
            assert auth is not None, 'no auth'

        if id is None:
            assert parent is not None, 'no page id'

        self.req = Request.from_token(authorization=auth)
        self.auth = auth
        if id is None:
            assert parent is not None
            res = self.req.post(database_create(), data=Database(parent=parent, properties=Properties(
                sche.Title(pname='name'),
            )))
            if isinstance(res, Database):
                id = res.id
                parent = res.parent
                self.id = id
            else:
                assert False, res.to_json(2)

        else:
            res = self.req.get(database_retrieve(id))
            assert isinstance(res, Database), res.to_json(2)
            parent = res.parent
            self.id = id
        self.object = res
        self.blocks = {}

        self._parent = parent
        self.cache_properties = []
        self.children = []
        self.multi_select_property = defaultdict(set)

    def create_page(self) -> 'NotionPage':
        from .page import NotionPage
        return NotionPage(auth=self.auth, parent=Parent.DataBaseParent(self.id))

    def properties(self):
        return self.object.properties

    def set_property(self, property_args: sche.Schema):
        self.cache_properties.append(property_args)

    def flush_property(self):
        return self.update_properies(self.cache_properties)

    def update_properies(self, property_list: List[sche.Schema]):
        p = Properties(*property_list)
        presp = self.req.patch(database_update(self.id), Database(properties=Properties(p)))
        if isinstance(presp, Database):
            self.object = presp
            return True, presp
        else:
            return False, presp
