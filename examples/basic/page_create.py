from potion import Request, NotionHeader
from potion.api import *
from potion.objects import *

token = ''

nh = NotionHeader(authorization=token)
req = Request(nh.headers)

properties = Properties(
    prop.Title('Name',
               rich_text=[
                   {
                       "text": {
                           "content": "Tuscan Kale"
                       }
                   }
               ]
               ),
    prop.Number('Price', 2.5),
    prop.MultiSelect('Args', [
        prop.MultiSelectOption(name='A'),
        prop.MultiSelectOption(name='B'),
    ])
)

data = Page(parent=Parent.DataBaseParent('7d39de23304d484ea079a35f816ae68f'),
            properties=properties
            )

print(data)
print(req.post(page_create(),
               data=data))
