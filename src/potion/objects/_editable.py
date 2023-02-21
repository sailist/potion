from typing import Dict

from potion.objects.user import User
from potion.utils.date import parse_notion_date


class Editable(Dict):
    @property
    def created_time(self):
        return parse_notion_date(self['created_time'])

    @property
    def last_edited_time(self):
        return parse_notion_date(self['last_edited_time'])

    @property
    def created_by(self):
        return User.SimpleUser(self['created_by'])

    @property
    def last_edited_by(self):
        return User.SimpleUser(self['last_edited_by'])
