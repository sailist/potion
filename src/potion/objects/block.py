from .common import NotionObject


class Block(NotionObject):
    union_type = 'dict'

    def __init__(self, **kwargs):
        super().__init__('',
                         kwargs=dict(**kwargs))

    def set_children(self, blocks):
        self['children'] = blocks

    @property
    def id(self):
        return self['id']

    @property
    def has_children(self):
        return self['has_children']

    @property
    def type(self):
        return self['type']


class Todo(Block):
    property_name = 'to_do'

    def __init__(self, rich_text=None, checked=None, color=None, children=None):
        super().__init__(rich_text=rich_text,
                         checked=checked,
                         color=color,
                         children=children)


class Callout(Block):

    def __init__(self, rich_text=None, icon=None, color=None, children=None):
        super().__init__(rich_text=rich_text,
                         icon=icon,
                         color=color,
                         children=children)


class Quote(Block):

    def __init__(self, rich_text=None, color=None, children=None):
        super().__init__(rich_text=rich_text,
                         color=color,
                         children=children)


class Code(Block):

    def __init__(self, rich_text=None, caption=None, language=None):
        super().__init__(rich_text=rich_text,
                         caption=caption,
                         language=language)


class Bulleted(Block):
    property_name = 'bulleted_list_item'

    def __init__(self, rich_text=None, color=None, children=None):
        super().__init__(rich_text=rich_text,
                         color=color,
                         children=children)

    @property
    def rich_text(self):
        return self['rich_text']

    @property
    def color(self):
        return self['color']

    @property
    def children(self):
        return self['children']


class Numbered(Bulleted):
    property_name = 'numbered_list_item'


class Toggle(Bulleted):
    property_name = 'toggle'


class _Headeing(Block):

    def __init__(self, rich_text=None, color=None):
        super().__init__(rich_text=rich_text,
                         color=color)


class Heading1(_Headeing):
    property_name = 'heading_1'


class Heading2(_Headeing):
    property_name = 'heading_2'


class Heading3(_Headeing):
    property_name = 'heading_3'
