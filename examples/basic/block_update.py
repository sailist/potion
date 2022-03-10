from potion import Request, NotionHeader
from potion.objects import *
from potion.api import *

token = ''

nh = NotionHeader(authorization=token)
req = Request(nh.headers)

data = block.Todo(checked=True)
print(data)

print(req.patch(url=block_retrieve('dc580d1ec13941c2a718b29933cfdcf4'), data=data))
