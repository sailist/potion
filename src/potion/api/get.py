from potion.urls import url


def database_retrieve(database_id):
    """
    get
    :param database_id:
    :return:
    """
    return url.databases(database_id)


def page_retrieve(page_id):
    """
    get
    :param page_id:
    :return:
    """
    return url.pages(page_id)


def page_property_retrieve(page_id, property_id):
    """
    get
    :param page_id:
    :param property_id:
    :return:
    """
    return url.pages(page_id, property_id)


def block_retrieve(block_id):
    """
    get
    :param block_id:
    :return:
    """
    return url.blocks(block_id)


def block_children_retrieve(block_id, page_size: int = 100, start_cursor=None):
    """
    get
    :param block_id:
    :param page_size:
    :return:
    """
    return url.blocks(block_id, page_size=page_size, start_cursor=start_cursor)


def user_retrieve(user_id):
    """
    get
    :param user_id:
    :return:
    """
    return url.users(user_id)


def users_list():
    """
    get
    :return:
    """
    return url.users()


def user_bot_retrieve():
    """
    get
    :return:
    """
    return url.users('me')
