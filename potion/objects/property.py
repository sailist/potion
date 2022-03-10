from datetime import datetime
from typing import List, Union

__all__ = ['Number', 'Select', 'MultiSelect', 'Date',
           'CheckBox', 'URL', 'Email', 'Phone', 'Property']

from .common import NotionObject, _Null


class Property(NotionObject): pass


class Title(Property):
    def __init__(self, pname: str, title):
        super().__init__(pname, args=title)


class Number(Property):
    def __init__(self, pname: str, number: float):
        super().__init__(pname, args=number)


class Select(Property):
    def __init__(self, pname, id=None, name=None, color=None):
        super().__init__(pname, kwargs=dict(id=id, name=name, color=color))

    @property
    def id(self):
        return self['id']

    @property
    def name(self):
        return self['name']

    @property
    def color(self):
        return self['color']


class MultiSelect(Property):
    property_name = 'multi_select'

    def __init__(self, pname, selects: Union[List[Select], _Null]):
        if isinstance(selects, list):
            selects = [i._value for i in selects]
        super().__init__(pname, args=selects)


class Date(Property):
    def __init__(self, pname, start: datetime, end: datetime, time_zone: str):
        kwargs = dict(start=start.isoformat(),
                      end=end.isoformat(),
                      time_zone=time_zone)
        super(Date, self).__init__(pname,
                                   kwargs=kwargs)


class SingleValueProperty(Property):
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


class Formula(Property):
    def __init__(self, pname: str):
        super().__init__(pname)
        raise NotImplementedError('Formula property is not supported currently.')


class Relation(Property):
    def __init__(self, pname: str):
        super().__init__(pname)
        raise NotImplementedError('Relation property is not supported currently.')


class Rollup(Property):
    def __init__(self, pname: str):
        super().__init__(pname)
        raise NotImplementedError('Rollup property is not supported currently.')


class People(Property):
    def __init__(self, pname: str):
        super().__init__(pname)
        raise NotImplementedError('People property is not supported currently.')


class Files(Property):
    def __init__(self, pname: str):
        super().__init__(pname)
        raise NotImplementedError('Files property is not supported currently.')
