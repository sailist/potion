from potion import Request, NotionHeader
from potion.objects import *
from potion.api import *

token = ''

nh = NotionHeader(authorization=token)
req = Request(nh.headers)

property_list = [
    sche.Title('Name'),
    sche.RichText('Description'),
    sche.CheckBox('In stock'),
    sche.Select('Food group',
                options=[
                    sche.Option('🥦Vegetable', 'green'),
                    sche.Option('🍎Fruit', 'red'),
                    sche.Option('💪Protein', 'yellow'),
                ]),
    sche.Number('Price', format='dollar'),
    sche.AnySchema('last ordered', 'date'),
    sche.MultiSelect('Store availability', [
        sche.Option('Duc Loi Market', ),
        sche.Option('Rainbow Grocery', 'gray'),
        sche.Option('Nijiya Market', 'purple'),
        sche.Option("Gus's Community Market", 'yellow'),
    ]),
    sche.AnySchema('+1', 'people'),
    sche.AnySchema('Photo', 'files'),
]

p = Properties(*property_list)

data = Database(
    parent=Parent.PageParent(page_id='a20f7d2442ce4004860541fbada2f61c'),
    title=[{
        "type": "text",
        "text": {
            "content": "Grocery List",
            "link": None
        }
    }],
    properties=p)

print(data)
print(req.post(url=database_create(),
               data=data))
