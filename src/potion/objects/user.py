from .common import NotionObject


class User(NotionObject):
    """
    {
        "object": "user",
        "id": "d40e767c-d7af-4b18-a86d-55c61f1e39a4",
        "type": "person",

        "person": {
            "email": "avo@example.org",
        },
        # or
        "bot": {
            "owner": {
              "type": "workspace",
              "workspace": true
            },
            "workspace_name": "haozhe's Notion"
        }
        "name": "Avocado Lovelace",
        "avatar_url": "https://secure.notion-static.com/e6a352a8-8381-44d0-a1dc-9ed80e62b53d.jpg",
    }

    {
        "object": "user",
        "id": "197fdf54-0a3b-449c-80fd-eb0c6d340c0e"
    }
    """

    def __init__(self,
                 name: str = None,
                 avatar_url: str = 'person',
                 type: str = None,
                 **kwargs):

        if type == 'people':
            pass
        elif type == 'bot':
            kwargs['bot'] = Bot(**kwargs['bot'])

        super().__init__(None, dict(
            name=name,
            avatar_url=avatar_url,
            type=type,
            **kwargs
        ))

    @property
    def object(self):
        return self['object']

    @property
    def type(self):
        return self['type']

    @property
    def is_people(self):
        return self.type == 'people'

    @property
    def is_bot(self):
        return self.type == 'bot'

    @property
    def bot(self):
        assert self.is_bot
        return self['bot']

    @property
    def people(self):
        assert self.is_people
        return self['people']

    @classmethod
    def SimpleUser(cls, id):
        return User(id=id)

    # def __init__(self, type=None, page_id=None, workspace: bool = None, database_id=None):
    #     super().__init__(None, kwargs=dict(type=type, page_id=page_id,
    #                                        workspace=workspace, database_id=database_id))


class Person(NotionObject):
    def __init__(self, email: str = None):
        super().__init__(None, dict(email=email))

    @property
    def email(self):
        return self['email']


class Bot(NotionObject):
    """
    "bot": {
        "owner": {
          "type": "workspace",
          "workspace": true
        },
        "workspace_name": "haozhe's Notion"
    }

    """

    def __init__(self, owner=None, workspace_name=None):
        if owner is not None:
            owner = Owner(**owner)
        super().__init__(None, dict(owner=owner, workspace_name=workspace_name))

    @property
    def owner(self):
        return

    @property
    def workspace_name(self):
        return self['workspace_name']


class Owner(NotionObject):
    def __init__(self, type=None,
                 workspace=None):
        super().__init__(None, dict(type=type, workspace=workspace))
