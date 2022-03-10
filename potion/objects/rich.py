from .common import NotionObject


class RichText(NotionObject):
    property_name = 'rich_text'


class Text(RichText):
    def __init__(self, content, link=None):
        super(Text, self).__init__(kwargs=dict(content=content, link=link))


class Link(RichText):
    """
    Text link objects contain a type key whose value is always "url" and a url key whose value is a web address
    """

    def __init__(self, url=None):
        super(Link, self).__init__(kwargs=dict(url=url))
