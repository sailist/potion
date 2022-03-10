from potion import Request, NotionHeader
from potion.objects import *
from potion.api import *

token = ''

nh = NotionHeader(authorization=token)
req = Request(nh.headers)

properties = Properties(
    prop.Title('Name',
               title=[
                   {
                       "text": {
                           "content": "Tuscan Kale"
                       }
                   }
               ]
               ),
    prop.Number('Price', 2.5),
)

data = Page(parent=Parent.DataBaseParent('84b3a4d21ccb4435889084f933c3fc04'),
            properties=properties
            )

print(data)
print(req.post(page_create(),
               data=data))
