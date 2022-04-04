import os
from collections import defaultdict
from datetime import datetime
from typing import Union, TYPE_CHECKING

from potion import Request
from potion.api import *
from potion.objects import Parent, Page, Properties
from potion.objects import block, rich, prop, Error as NotionError

from .base import NotionObject

if TYPE_CHECKING:
    from .database import NotionDatabase


class NotionPage(NotionObject):
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
            res = self.req.post(page_create(), data=Page(parent=parent, properties=Properties()))
            if isinstance(res, Page):
                id = res.id
                self.id = id
            else:
                assert False, res.to_json(2)
        else:
            res = self.req.get(page_retrieve(id))
            assert isinstance(res, Page), res.to_json(2)
            self.id = id
        self.object = res
        self.blocks = {}

        self._parent = parent

        self.properties = []
        self.children = []
        self.multi_select_property = defaultdict(set)

    def flush_property(self):
        for property_name, values in self.multi_select_property.items():
            self.properties.append(prop.MultiSelect(property_name, selects=[
                prop.MultiSelectOption(name=v) for v in values
            ]))

        page = Page(properties=Properties(*self.properties))
        res = self.req.patch(
            url=page_update(self.id),
            data=page
        )
        self.properties.clear()
        if isinstance(res, NotionError):
            print(res)
        return res

    def flush_children(self):
        page = Page(children=self.children)
        res = self.req.patch(
            url=block_children_append(self.id),
            data=page
        )
        self.children.clear()
        if isinstance(res, NotionError):
            print(res)
        return res

    def append_content(self, content: Union[dict, block.Block]):
        self.children.append(content)

    def append_code(self, code, language='python'):
        code = [code[i:i + 1999] for i in range(0, len(code), 1999)]
        content = block.Code(rich_text=[rich.Text(f"{i}") for i in code][:100], language=language)
        self.append_content(content)

    def create_database(self) -> 'NotionDatabase':
        from .database import NotionDatabase
        self.flush_children()
        return NotionDatabase(auth=self.auth, parent=Parent.PageParent(self.id))

    @property
    def title_property_name(self):
        for prop_name in self.object.properties:
            if self.object.properties[prop_name]['id'] == 'title':
                return prop_name

    def set_title(self, value: str):
        self.properties.append(prop.Title(self.title_property_name,
                                          rich_text=[rich.Text(content=value)]))

    def set_text(self, property_name, value):
        value = f'{value}'
        self.properties.append(prop.RichTextProp(property_name,
                                                 rich_text=[rich.Text(content=value)]))

    def set_duration(self, property_name: str, start: datetime = None, end: datetime = None):
        self.properties.append(prop.Date(property_name, start=start, end=end))

    def set_checkbox(self, property_name: str, checkbox=True):
        self.properties.append(prop.CheckBox(property_name, checkbox))

    def set_number(self, property_name: str, number):
        self.properties.append(prop.Number(property_name, number))

    def add_option(self, property_name, value):
        if value is None:
            return
        else:
            value = f'{value}'
        self.multi_select_property[property_name].add(value)
        self.properties.append(prop.MultiSelect(pname=property_name, selects=[
            prop.MultiSelectOption(name=value)
        ]))

    def remove_option(self, property_name, value):
        if value in self.multi_select_property[property_name]:
            self.multi_select_property[property_name].remove(value)
