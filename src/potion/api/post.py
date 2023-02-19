from potion.urls import url


def database_create():
    """https://developers.notion.com/reference/create-a-database"""
    return url.databases()


def database_query(database_id, ):
    """https://developers.notion.com/reference/post-database-query"""
    return url.databases(database_id, query=True)


def page_create():
    """https://developers.notion.com/reference/post-page"""
    return url.pages()


def search():
    """https://developers.notion.com/reference/post-search"""
    return url.search()


def comment_create():
    """https://developers.notion.com/reference/create-a-comment"""
    return url.comment()
