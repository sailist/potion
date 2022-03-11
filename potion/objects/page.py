from typing import Union, List, Dict

from potion.objects import NotionObject
from potion.objects.block import Block
from potion.objects.common import Properties, Parent
from potion.objects.property import Property


class Page(NotionObject):
    union_type = 'dict'

    def __init__(self,
                 parent: Union[Parent, Dict] = None,
                 title=None,
                 icon=None,
                 properties: Union[Properties, List[Property]] = None,
                 children: List[Union['Block', Dict]] = None, **kwargs):
        if isinstance(parent, dict):
            parent = Parent(**parent)
        if isinstance(properties, list):
            properties = Properties(*properties)

        super().__init__(None,
                         kwargs=dict(parent=parent,
                                     title=title,
                                     icon=icon,
                                     children=children,
                                     properties=properties,
                                     **kwargs))

    @property
    def parent(self):
        return self['parent']

    @property
    def properties(self):
        return self['properties']

    @property
    def object(self):
        return self['object']

    @property
    def id(self):
        return self['id']

    @property
    def created_time(self):
        return self['created_time']

    @property
    def last_edited_time(self):
        return self['last_edited_time']

    @property
    def created_by(self):
        return self['created_by']

    @property
    def last_edited_by(self):
        return self['last_edited_by']

    @property
    def archived(self):
        return self['archived']

    @property
    def url(self):
        return self['url']
