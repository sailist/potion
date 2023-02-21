from potion.objects import *


def parse(dic: dict) -> NotionObject:
    if dic['object'] == 'error':
        return Error(**dic)
    elif dic['object'] == 'page':
        return Page(**dic)
    elif dic['object'] == 'database':
        return Database(**dic)
    elif dic['object'] == 'block':
        return Block(**dic)
    elif dic['object'] == 'list':
        return Pagination(**dic)
    elif dic['object'] == 'user':
        return User(**dic)
        # pass
    return dic


def format_query(**kwargs):
    return '?' + '&'.join([f'{k}={v}' for k, v in kwargs.items() if v is not None])
