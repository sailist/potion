import os

from potion.objects import Page, Database
from dbrecord import PDict


def title(res):
    if res['object'] == 'page':
        for k, v in res['properties'].items():
            if v['type'] == 'title':
                return ''.join([i['plain_text'] for i in v['title']])
    else:
        return ''.join([i['plain_text'] for i in res['title']])


def write_database(res, pages, root):
    for k, v in res['properties'].items():
        if v['id'] == 'title':
            title_key = k
            break

    lis = []
    basetitle = f"{to_filename(title(res))}-{res['id']}"
    for page in pages:
        fname = write_page(page, os.path.join(root, basetitle))
        lis.append(fname)
        print(fname)

    with open(os.path.join(root, basetitle + '.txt'), 'w') as w:
        w.write('\n'.join(lis))


def write_page(res, root):
    basetitle = f"{to_filename(title(res))}-{res['id']}.json"
    fname = os.path.join(root, basetitle)
    os.makedirs(os.path.dirname(fname), exist_ok=True)
    with open(fname, 'w') as w:
        w.write(res.to_json())
    return fname


import re

_invalid_fc = (
    r"[+?@#$&%*()=;|,<>: +"
    r"\^\-\/\t\b\[\]\"]+"
)


def to_filename(basename):
    return re.sub(_invalid_fc, '_', basename)


def render():
    dic = PDict('notion-backup.sqlite')
    tree = {}
    reverse = {}
    roots = set()

    def walk(notion_id):
        _pages = []
        _databases = []
        if notion_id in tree:
            for children in tree[notion_id]:
                if dic[children]['object'] == 'page':
                    _pages.append(children)
                else:
                    _databases.append(children)

        yield [notion_id], _pages, _databases
        for sub in _pages:
            for subroot, _pages, _databases in walk(sub):
                yield [notion_id, *subroot], _pages, _databases
        for sub in _databases:
            for subroot, _pages, _databases in walk(sub):
                yield [notion_id, *subroot], _pages, _databases

    for k, v in dic.items():
        if v['parent']['type'] == 'workspace':
            roots.add(v['id'])
            continue

        parent_id = v['parent'][v['parent']['type']]
        reverse[k] = parent_id
        tree.setdefault(parent_id, []).append(k)

    for k in reverse:
        parent = reverse[k]
        while parent in reverse:
            parent = reverse[parent]
        roots.add(parent)
    path = {}
    for root in roots:
        for cur, pages, databases in walk(root):
            if cur[-1] not in dic:
                continue

            res = dic[cur[-1]]
            basetitle = f"{to_filename(title(res))}-{cur[-1]}"
            if basetitle == '':
                basetitle = 'untitled'
            path[cur[-1]] = basetitle

            basepath = os.path.join('backup', *[path.get(i, i) for i in cur[:-1]], basetitle)

            if isinstance(res, Page):
                if len(pages) > 0:
                    os.makedirs(basepath, exist_ok=True)
                write_page(res, os.path.dirname(basepath))
                for page in pages:
                    # cur/{page}.md
                    write_page(dic[page], basepath)
            elif isinstance(res, Database):
                os.makedirs(basepath, exist_ok=True)
                write_database(res, [dic[i] for i in pages], os.path.dirname(basepath))
