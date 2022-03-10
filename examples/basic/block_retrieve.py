from potion import Request, NotionHeader
from potion.api import *

token = ''

nh = NotionHeader(authorization=token)
req = Request(nh.headers)

print(req.get(url=block_retrieve('9428c7d74854444389d22845127e585e')))
