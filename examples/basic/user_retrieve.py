from potion import Request, NotionHeader
from potion.api import *

token = ''

nh = NotionHeader(authorization=token)
req = Request(nh.headers)

print(req.get(url=user_bot_retrieve()))
print(req.get(url=user_retrieve('')))
print(req.get(url=users_list()))
