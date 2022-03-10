from potion import Request, NotionHeader
from potion.api import *

token = ''

nh = NotionHeader(authorization=token)
req = Request(nh.headers)

print(req.get(url=database_retrieve('1bb0f79b87584afe8609d6e248285cfb')))
