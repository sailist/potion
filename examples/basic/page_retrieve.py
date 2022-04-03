from potion import Request, NotionHeader
from potion.api import *

token = 'secret_hOmuqFq4VNBwfX11MQfy8mVE3YamSuWpysRltnxq2xt'

nh = NotionHeader(authorization=token)
req = Request(nh.headers)

print(req.get(url=page_retrieve('190a7b9ace9d4bd5b642f9a7114775e5')))

# https://www.notion.so/ReadList-190a7b9ace9d4bd5b642f9a7114775e5