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
