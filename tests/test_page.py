"""
https://developers.notion.com/reference/patch-block-children
"""
from potion import Request, NotionHeader
from potion.api import *
from potion.objects import *
from potion.utils.date import strftime

currentdt = strftime()
token = 'secret_BiBCJMpKdXapCh3a0I8TGTGzeNlKbXEGBNZlzhAgl84'


# 每次基于一个 database 创建一个 page 实例，在 page 里插入一个 database，同时该 page 再创建别的 block 并删除

class TestAll:

    def test_database_create(self, page_id):
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
            parent=Parent.PageParent(page_id=page_id),
            title=[{
                "type": "text",
                "text": {
                    "content": f"potion-test-{currentdt}",
                    "link": None
                }
            }],
            properties=p)

        resp = req.post(url=database_create(),
                        data=data)
        print(resp)
        assert resp.object == 'database'
        database_id = resp.id
        return database_id

    def test_page_create(self, database_id):
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
        )

        data = Page(parent=Parent.DataBaseParent(database_id),
                    properties=properties
                    )

        print(data)
        resp = (req.post(page_create(),
                         data=data))
        print(resp)
        assert resp['object'] == 'page'


def test_append():
    pass
# data = Page(children=[
#     block.Todo(rich_text=[], checked=True, color=Color.blue_background),
#     block.Heading2(rich_text=[{"type": "text", "text": {"content": "Lacinato kale"}}]),
#     {
#         "type": "heading_2",
#         "heading_2": {
#             "rich_text": [{"type": "text", "text": {"content": "Lacinato kale"}}]
#         }
#     },
# ])
# res = req.patch(url=block_children_append('f854bfdf24d24629b3f5c43f40d15a20'),  # a page_id
#                 data=data)
# assert res.object == 'list'

# req.get(url=block_retrieve())
