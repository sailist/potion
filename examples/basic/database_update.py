from potion import Request, NotionHeader
from potion.api import *
from potion.objects import *

token = ''

nh = NotionHeader(authorization=token)
req = Request(nh.headers)

property_list = [
    sche.DeleteSchema('+1'),
    sche.URL('Photo'),
    sche.MultiSelect('Store availability', [
        sche.Option('Duc Loi Market'),
        sche.Option('Rainbow Grocery'),
        sche.Option('Gus\'s Community Market'),
        sche.Option('The Good Life Grocery', color='orange'),
    ])
]

print(sche.DeleteSchema('+1'))

properties = Properties(*property_list)

data = Database(
    title=[{
        "text": {
            "content": "Today's grocery list",
        }
    }],
    properties=properties)

print(data)
print(req.patch(url=database_update('1bb0f79b87584afe8609d6e248285cfb'),
                data=data))
