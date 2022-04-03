import os

from potion import Request
from potion.api import *
from potion.objects import Parent
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .page import NotionPage
    from .database import NotionDatabase


class NotionObject:
    def __init__(self, auth: str = None, id: str = None, parent: Parent = None):
        if auth is None:
            auth = os.environ.get('NOTION_SECRET', None)
            assert auth is not None, 'no auth'

        self.id = id

        self.req = Request.from_token(authorization=auth)
        self.auth = auth
        self.object = None

        self._parent = parent
        res = self.req.get(user_bot_retrieve())
        print(res)

    @property
    def parent(self):
        if self._parent.is_page:
            return self.parent_page
        elif self._parent.is_database:
            return self.parent_database
        return None

    def __str__(self):
        return str(self.object)

    @property
    def parent_page(self) -> 'NotionPage':
        from .page import NotionPage
        if self._parent.is_page:
            res = NotionPage(auth=self.auth, id=self._parent.id)
            return res

    @property
    def parent_database(self) -> 'NotionDatabase':
        if self._parent.is_page:
            from .database import NotionDatabase
            res = NotionDatabase(auth=self.auth, id=self._parent.id)
            return res
