def databases(database_id='', query=False):
    query_str = '/query' if query else ''
    return f'https://api.notion.com/v1/databases/{database_id}{query_str}'


def pages(page_id='', property_id=None):
    property_str = f'/properties/{property_id}' if property_id is not None else ''
    return f'https://api.notion.com/v1/pages/{page_id}{property_str}'


def blocks(block_id='', page_size=None, start_cursor=None, append=False):
    assert page_size is None or isinstance(page_size, int)
    # assert start_cursor is None or isinstance(start_cursor, star)

    if append:
        children_str = f'/children'
    else:
        children_strs = []
        if page_size is not None:
            children_strs.append(f'page_size={page_size}')
        if start_cursor is not None:
            children_strs.append(f'start_cursor={start_cursor}')
        children_strs = '&'.join(children_strs)
        children_str = f'/children?{children_strs}'
    return f"https://api.notion.com/v1/blocks/{block_id}{children_str}"


def blocks_cursor(block_id='', page_size=None, start_cursor=None):
    assert page_size is None or isinstance(page_size, int)
    return f"https://api.notion.com/v1/blocks/{block_id}/children?"


def users(user_id=''):
    return f'https://api.notion.com/v1/users/{user_id}'


def search():
    return 'https://api.notion.com/v1/search'
