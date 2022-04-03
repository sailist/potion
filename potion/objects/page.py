from typing import Union, List, Dict

from potion.objects import NotionObject
from potion.objects.block import Block
from potion.objects.common import Properties, Parent
from potion.objects.property import Property


class Page(NotionObject):
    """
    For appending blocks
    ```python
    Page(children=[
        block.Todo(rich_text=[], checked=True, color=Color.blue_background),
        block.Heading2(rich_text=[{"type": "text", "text": {"content": "Lacinato kale"}}]),
        {
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "Lacinato kale"}}]
            }
        },
    ])
    ```
    For create page
    ```python
    properties = Properties(
        prop.Title('Name',
                   rich_text=[
                       {
                           "text": {
                               "content": "Tuscan Kale"
                           }
                       }
                   ]
                   ),
        prop.Number('Price', 2.5),
        prop.MultiSelect('Args', [
            prop.MultiSelectOption(name='A'),
            prop.MultiSelectOption(name='B'),
        ])
    )

    data = Page(parent=Parent.DataBaseParent('7d39de23304d484ea079a35f816ae68f'),
                properties=properties
                )
    ```
    """
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

        self.load_mark('parent')
        self.load_mark('properties')

    @property
    def string_title(self) -> str:
        for k, v in self['properties'].items():
            if v['id'] == 'title':
                return ''.join([t['plain_text'] for t in v['title']])
        return self.id

    @property
    def parent(self) -> Parent:
        return self['parent']


    @property
    def properties(self) -> Properties:
        return self['properties']

    @property
    def object(self):
        return self['object']

    @property
    def short_id(self):
        return self.id[:4]

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

    def set_children(self, blocks):
        self['children'] = blocks
