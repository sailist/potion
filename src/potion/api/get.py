from potion.urls import url


def database_retrieve(database_id):
    """
    https://developers.notion.com/reference/retrieve-a-database

    Args:
        database_id:

    Returns:

    """
    return url.databases(database_id)


def page_retrieve(page_id):
    """https://developers.notion.com/reference/retrieve-a-page"""
    return url.pages(page_id)


def page_property_retrieve(page_id, property_id):
    """https://developers.notion.com/reference/retrieve-a-page-property"""
    return url.pages(page_id, property_id)


def block_retrieve(block_id):
    """https://developers.notion.com/reference/retrieve-a-block"""
    return url.blocks(block_id)


def block_children_retrieve(block_id, page_size: int = 100, start_cursor=None):
    """https://developers.notion.com/reference/get-block-children"""
    return url.blocks(block_id, page_size=page_size, start_cursor=start_cursor)


def user_retrieve(user_id):
    """https://developers.notion.com/reference/get-user"""
    return url.users(user_id)


def users_list():
    """https://developers.notion.com/reference/get-users"""
    return url.users()


def user_bot_retrieve():
    """https://developers.notion.com/reference/get-self"""
    return url.users('me')


def comment_retrieve(block_id):
    """https://developers.notion.com/reference/retrieve-a-comment"""
    return url.comment(block_id)
