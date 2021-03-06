"""
https://developers.notion.com/reference/patch-block-children
"""
from potion import Request, NotionHeader
from potion.api import *
from potion.objects import *

token = ''

nh = NotionHeader(authorization=token)
req = Request(nh.headers)

data = Page(children=[
    block.Todo(rich_text=[], checked=True, color=Color.blue_background),
    block.Heading2(rich_text=[{"type": "text", "text": {"content": "Lacinato kale"}}]),
    {
        "type": "heading_2",
        "heading_2": {
            "rich_text": [{"type": "text", "text": {"content": "Lacinato kale"}}]
        }
    },
])
print(data)
# print(req.patch(url=block_children_append('a20f7d2442ce4004860541fbada2f61c'),  # a page_id
#                 data=data))
