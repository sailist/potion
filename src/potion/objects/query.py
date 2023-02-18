from .common import NotionObject


class Condition(NotionObject):
    def __init__(self, *properties):
        super().__init__('', args=properties)


class And(Condition): pass


class Or(Condition): pass


class SortProperty(NotionObject):
    def __init__(self, property=None, direction='ascending'):
        super().__init__(None, kwargs={'property': property, 'direction': direction})


class QueryProperty(NotionObject):
    """
    see https://developers.notion.com/reference/post-database-query-filter for details
    """
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

    def __init__(self, pname: str, conditions: Condition):
        super().__init__(pname, args=conditions)

    @staticmethod
    def Search(conditions: Condition):
        return Filter(None, conditions)

    @staticmethod
    def QueryDatabase(filter: Condition):
        return Filter('', filter)


class Sorts(NotionObject):
    property_name = 'sorts'

    def __init__(self, *sorts):
        super().__init__('', args=sorts)


class Search(NotionObject):

    def __init__(self, query: str = None, sort=None, filter=None, start_cursor: str = None, page_size: int = None):
        super().__init__(None, kwargs={
            'query': query,
            'sort': sort,
            'filter': filter,
            'start_cursor': start_cursor,
            'page_size': page_size,
        })
