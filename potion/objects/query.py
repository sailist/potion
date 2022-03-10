from .common import NotionObject


class Condition(NotionObject):
    def __init__(self, *properties):
        super().__init__('', args=properties)


class And(Condition): pass


class Or(Condition): pass


class QueryProperty(NotionObject):
    union_type = 'dict'

    def __init__(self, property_name: str, property_type: str, conditions: str, condition_value):
        super().__init__(None, kwargs={
            'property': property_name,
            property_type: {
                conditions: condition_value
            }
        })


class Filter(NotionObject):
    union_type = 'dict'

    def __init__(self, conditions: Condition):
        super().__init__('', args=conditions)


class Sort(NotionObject):
    property_name = 'sorts'


class Search(NotionObject):

    def __init__(self, query: str, sort=None, filter=None, start_cursor: str = None, page_size: int = None):
        super().__init__(None, kwargs={
            'query': query,
            'sort': sort,
            'filter': filter,
            'start_cursor': start_cursor,
            'page_size': page_size,
        })
