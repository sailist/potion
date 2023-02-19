from potion.urls import url


def database_update(database_id):
    """https://developers.notion.com/reference/update-a-database"""
    return url.databases(database_id)


def page_update(page_id):
    """https://developers.notion.com/reference/patch-page"""
    return url.pages(page_id)


def block_update(block_id):
    """https://developers.notion.com/reference/update-a-block"""
    return url.blocks(block_id)


def block_children_append(block_id):
    """https://developers.notion.com/reference/patch-block-children"""
    return url.blocks(block_id, append=True)
