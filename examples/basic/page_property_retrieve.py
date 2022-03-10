from objects.common import Properties
from potion import Request, NotionHeader
from potion.objects import *
from potion.api import *

token = ''

nh = NotionHeader(authorization=token)
req = Request(nh.headers)

print(req.get(url=page_property_retrieve('94e35af6eb3d456c9e1b6130ba23494e', 'title')))
