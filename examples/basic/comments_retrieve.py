"""
https://developers.notion.com/reference/retrieve-a-comment
"""
from potion import Request, NotionHeader
from potion.api import *

token = ''

nh = NotionHeader(authorization=token)
req = Request(nh.headers)

print(req.get(url=comment_retrieve('<block_id>')))
