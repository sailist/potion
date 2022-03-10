from objects.common import Properties
from potion import Request, NotionHeader
from potion.objects import *
from potion.api import *

raise NotImplementedError()

token = ''

nh = NotionHeader(authorization=token)
req = Request(nh.headers)

data = None
print(data)
print(req.post(url=database_create(),
               data=data))
