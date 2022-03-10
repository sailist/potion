"""
https://developers.notion.com/reference/post-database-query-filter
"""
from potion import Request, NotionHeader
from potion.api import *
from potion.objects import *

token = ''

nh = NotionHeader(authorization=token)
req = Request(nh.headers)

data = Filter(
    query.Or(
        {
            "property": "Done",
            "checkbox": {
                "equals": True
            }
        },
        query.QueryProperty(property_name='Done',
                            property_type=FilterProperty.checkbox,
                            conditions=FilterCondition.Checkbox.equals,
                            condition_value=True),
        query.And(
            {
                "property": "Food group",
                "select": {
                    "equals": "🥦Vegetable"
                }
            },
            query.QueryProperty(property_name='Food group',
                                property_type='select',
                                conditions='equals',
                                condition_value='🥦Vegetable'),
            {
                "property": "Is protein rich?",
                "checkbox": {
                    "equals": True
                }
            }),
    )
)
print(data)
print(req.post(url=database_create(),
               data=data))
