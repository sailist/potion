from potion import Request, NotionHeader
from potion.objects import *
from potion.api import *

token = ''

nh = NotionHeader(authorization=token)
req = Request(nh.headers)

data = Page(properties=Properties(prop.CheckBox('In stock', True)))
print(data)
print(req.patch(url=page_update('94e35af6eb3d456c9e1b6130ba23494e'), data=data))
