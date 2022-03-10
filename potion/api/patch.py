from potion.urls import url


def database_update(database_id):
    """
    patch
    :param database_id:
    :return:
    """
    return url.databases(database_id)


def page_update(page_id):
    """
    patch
    :param page_id:
    :return:
    """
    return url.pages(page_id)


def block_update(block_id):
    """
    patch
    :param block_id:
    :return:
    """
    return url.blocks(block_id)


def block_children_append(block_id):
    """
    patch
    :param block_id:
    :return:
    """
    return url.blocks(block_id, append=True)
