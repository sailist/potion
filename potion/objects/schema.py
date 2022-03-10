from datetime import datetime
from typing import List

__all__ = ['Number', 'Select', 'MultiSelect', 'Date', 'Option',
           'CheckBox', 'URL', 'Email', 'Phone', 'Title', 'RichText']

from .common import NotionObject, Any


class Schema(NotionObject): pass


class AnySchema(Any): pass


class Title(Schema):
    def __init__(self, pname: str):
        super().__init__(pname)


class RichText(Schema):
    property_name = 'rich_text'

    def __init__(self, pname: str):
        super().__init__(pname)


class Number(Schema):
    def __init__(self, pname: str, format: str):
        super().__init__(pname, kwargs=dict(format=format))


class Option(Schema):
    def __init__(self, name, color=None):
        super().__init__(None, kwargs=dict(name=name, color=color))

    def to_dict(self):
        val = {
            'name': self['name'],
        }
        if self['color'] is not None:
            val['color'] = self['color']
        return val


class Options(Schema):
    def __init__(self, options: List[Option]):
        super().__init__('', args=options)


class Select(Schema):
    def __init__(self, pname, options: List[Option]):
        super().__init__(pname, args=Options(options))


class MultiSelect(Schema):
    property_name = 'multi_select'
    include_type = True

    def __init__(self, pname, options: List[Option]):
        super().__init__(pname, args=Options(options))


class Date(Schema):
    def __init__(self, pname, start: datetime, end: datetime, time_zone: str):
        kwargs = dict(start=start.isoformat(),
                      end=end.isoformat(),
                      time_zone=time_zone)
        super(Date, self).__init__(pname,
                                   kwargs=kwargs)


class SingleValueProperty(Schema):
    def __init__(self, pname: str, value=None):
        super().__init__(pname, args=value)


class CheckBox(SingleValueProperty):
    """
    当 check = None 时，输出格式为
    {
      "Done?": {
        "checkbox": {}
      }
    }
    否则为单值
    """

    def __init__(self, pname: str, check: bool = None):
        super().__init__(pname, value=check)


class URL(SingleValueProperty):
    def __init__(self, pname: str, url: str = None):
        super().__init__(pname, value=url)


class Email(SingleValueProperty):
    def __init__(self, pname: str, email: str = None):
        super().__init__(pname, value=email)


class Phone(SingleValueProperty):
    def __init__(self, pname: str, phone_number: str = None):
        super().__init__(pname, value=phone_number)


class Formula(Schema):
    def __init__(self, pname: str):
        super().__init__(pname)
        raise NotImplementedError('Formula property is not supported currently.')


class Relation(Schema):
    def __init__(self, pname: str):
        super().__init__(pname)
        raise NotImplementedError('Relation property is not supported currently.')


class Rollup(Schema):
    def __init__(self, pname: str):
        super().__init__(pname)
        raise NotImplementedError('Rollup property is not supported currently.')


class People(Schema):
    def __init__(self, pname: str):
        super().__init__(pname)
        raise NotImplementedError('People property is not supported currently.')


class Files(Schema):
    def __init__(self, pname: str):
        super().__init__(pname)
        raise NotImplementedError('Files property is not supported currently.')
