from potion.urls import url


def block_delete(block_id):
    """https://developers.notion.com/reference/delete-a-block"""
    return url.blocks(block_id)
