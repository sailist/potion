def databases(database_id='', query=False):
    query_str = '/query' if query else ''
    return f'https://api.notion.com/v1/databases/{database_id}{query_str}'


def pages(page_id='', property_id=None):
    property_str = f'/properties/{property_id}' if property_id is not None else ''
    return f'https://api.notion.com/v1/pages/{page_id}{property_str}'


def blocks(block_id='', page_size=None, append=False):
    assert page_size is None or isinstance(page_size, int)

    if append:
        children_str = f'/children'
    else:
        children_str = f'/children?page_size={page_size}' if page_size is not None else ''
    return f"https://api.notion.com/v1/blocks/{block_id}{children_str}"


def users(user_id=''):
    return f'https://api.notion.com/v1/users/{user_id}'


def search():
    return 'https://api.notion.com/v1/search'
