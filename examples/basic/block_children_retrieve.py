"""
https://developers.notion.com/reference/get-block-children
"""
from potion import Request, NotionHeader
from potion.api import *

token = ''

nh = NotionHeader(authorization=token)
req = Request(nh.headers)

# https://www.notion.so/Lumo-Experiments-a20f7d2442ce4004860541fbada2f61c
print(req.get(url=block_children_append('a20f7d2442ce4004860541fbada2f61c')))
