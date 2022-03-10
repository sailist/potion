from typing import Union, List, Dict

from potion.objects import NotionObject
from potion.objects.property import Property
from potion.objects.common import Properties, Parent


class Page(NotionObject):
    union_type = 'dict'

    def __init__(self,
                 parent: Union[Parent, Dict] = None,
                 title=None,
                 icon=None,
                 properties: Union[Properties, List[Property]] = None,
                 children=None, **kwargs):
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
