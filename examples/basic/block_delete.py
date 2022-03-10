from potion import Request, NotionHeader
from potion.api import *

token = ''

nh = NotionHeader(authorization=token)
req = Request(nh.headers)

print(req.delete(url=block_delete('f64813d544a2458ba3d0cb00aedaf5ea')))
