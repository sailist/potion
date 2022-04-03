"""
Database objects describe the property schema of a database in Notion.
Pages are the items (or children) in a database.
Page property values must conform to the property objects laid out in the parent database object.

"""

from .common import NotionObject, Parent


class Database(NotionObject):
    union_type = 'dict'

    def __init__(self, parent=None, title=None, icon=None, properties=None, **kwargs):
        if isinstance(parent, dict):
            parent = Parent(**parent)

        super().__init__(None,
                         kwargs=dict(parent=parent,
                                     title=title,
                                     icon=icon,
                                     properties=properties,
                                     **kwargs))

    @property
    def short_id(self):
        return self.id[:4]

    @property
    def string_title(self):
        return ''.join([i['plain_text'] for i in self.title])

    @property
    def parent(self) -> Parent:
        return self['parent']

    @property
    def title(self):
        return self['title']

    @property
    def icon(self):
        return self['icon']

    @property
    def properties(self):
        return self['properties']

    @property
    def object(self) -> str:
        return self['object']

    @property
    def id(self) -> str:
        return self['id']

    @property
    def created_time(self):
        return self['created_time']

    @property
    def created_by(self):
        return self['created_by']

    @property
    def last_edited_by(self):
        return self['last_edited_by']

    @property
    def last_edited_time(self):
        return self['last_edited_time']

    @property
    def url(self) -> str:
        return self['url']

    @property
    def archived(self) -> bool:
        return self['archived']
