from potion.objects.common import NotionObject


class Comment(NotionObject):
    def __init__(self, **kwargs):
        super().__init__(None, dict(**kwargs))

    @property
    def discussion_id(self):
        return self['discussion_id']

    @property
    def id(self):
        return self['id']
