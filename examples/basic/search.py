"""
https://developers.notion.com/reference/post-database-query-filter
"""
from potion import Request, NotionHeader
from potion.api import *
from potion.objects import *

token = ''

nh = NotionHeader(authorization=token)
req = Request(nh.headers)

data = Search(query='External tasks',
              sort={
                  "direction": "ascending",
                  "timestamp": "last_edited_time"
              })

print(data)
print(req.post(url=search(),
               data=data))
