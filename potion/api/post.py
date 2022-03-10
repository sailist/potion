from potion.urls import url


def database_create():
    """
    post
    :return:
    """
    return url.databases()


def database_query(database_id, ):
    """
    post
    :param database_id:
    :return:
    """
    return url.databases(database_id, query=True)


def page_create():
    """
    post
    :return:
    """
    return url.pages()


def search():
    """
    post
    :return:
    """
    return url.search()
