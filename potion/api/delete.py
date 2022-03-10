from potion.urls import url


def block_delete(block_id):
    """
    delete
    :param block_id:
    :return:
    """
    return url.blocks(block_id)
