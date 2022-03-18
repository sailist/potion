import sys, os
import time
from typing import Union
from tqdm import tqdm
from dbrecord.pdict import PDict
from potion import Request, NotionHeader
from potion.api import *
from potion.objects import *


def recursive_parsechild(parent: Union[Page, Block], pid):
    has_more = True
    blocks = []
    start_cursor = None
    while has_more:
        pag = req.get(url=block_children_retrieve(pid, start_cursor=start_cursor))
        if isinstance(pag, Pagination):
            has_more = pag.has_more
            start_cursor = pag.next_cursor
            for block in pag.results:
                if isinstance(block, Block):
                    if block.has_children and block.type not in {'child_page', 'child_database'}:
                        recursive_parsechild(block, block.id)
                blocks.append(block)
        else:
            time.sleep(1)
            continue

    parent.set_children(blocks)

    return parent


def full_backup(req, base_path):
    object_value = PDict(os.path.join(base_path, 'notion-backup.sqlite'))

    has_more = True
    start_cursor = None

    skiped, updated = 0, 0
    while has_more:
        data = Search(query='',
                      sort={
                          "direction": "ascending",
                          "timestamp": "last_edited_time"
                      },
                      page_size=0,
                      start_cursor=start_cursor)
        pag = req.post(url=search(),
                       data=data)

        if isinstance(pag, Pagination):
            has_more = pag.has_more
            start_cursor = pag.next_cursor
            for res in tqdm(pag.results):
                if res.id in object_value:
                    if object_value[res.id]['last_edited_time'] == res.last_edited_time:
                        skiped += 1
                        continue

                if isinstance(res, Page):
                    res = recursive_parsechild(res, res.id)
                elif isinstance(res, Database):
                    pass
                else:
                    raise NotImplementedError()

                object_value[res.id] = res
                updated += 1
        else:
            time.sleep(0.5)
            continue
    object_value.flush()

    return skiped, updated


if __name__ == '__main__':
    args = list(sys.argv[1:])
    if len(args) < 2:
        print('python -m potion.backup {token} {path}')
        exit(1)

    token, base_path, *_ = sys.argv[1:]

    os.makedirs(base_path, exist_ok=True)

    nh = NotionHeader(authorization=token)
    req = Request(nh.headers)

    skiped, updated = full_backup(req, base_path)
    print(f'Notion backup finished. {skiped} skiped, {updated} updated.')
    exit(0)
