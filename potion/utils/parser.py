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
    return dic
