from potion.utils.parser import format_query


def databases(database_id='', query=False):
    query_str = '/query' if query else ''
    return f'https://api.notion.com/v1/databases/{database_id}{query_str}'


def pages(page_id='', property_id=None):
    property_str = f'/properties/{property_id}' if property_id is not None else ''
    return f'https://api.notion.com/v1/pages/{page_id}{property_str}'


def blocks(block_id='', page_size=None, start_cursor=None, append=False):
    assert page_size is None or isinstance(page_size, int)
    params = format_query(page_size=page_size, start_cursor=start_cursor)
    children_str = f'/children{params}'
    return f"https://api.notion.com/v1/blocks/{block_id}{children_str}"


def blocks_cursor(block_id='', page_size=None, start_cursor=None):
    assert page_size is None or isinstance(page_size, int)
    params = format_query(page_size=page_size, start_cursor=start_cursor)
    return f"https://api.notion.com/v1/blocks/{block_id}/children{params}"


def users(user_id=''):
    return f'https://api.notion.com/v1/users/{user_id}'


def search():
    return 'https://api.notion.com/v1/search'


def comment(block_id=None, start_cursor=None, page_size=None):
    if block_id is not None:
        params = format_query(block_id=block_id, start_cursor=start_cursor, page_size=page_size)
        return f'https://api.notion.com/v1/comments{params}'
    return 'https://api.notion.com/v1/comments'
