from typing import List

__all__ = ['Number', 'Select', 'MultiSelect', 'Date', 'Option',
           'CheckBox', 'URL', 'Email', 'Phone', 'Title', 'RichText']

from .common import NotionObject, Any, Null


class Schema(NotionObject): pass


class AnySchema(Any): pass


class DeleteSchema(Schema):
    def __init__(self, pname: str):
        super().__init__(pname, args=Null)


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


class SingleValueSchema(Schema):
    def __init__(self, pname: str):
        super().__init__(pname)


class Date(SingleValueSchema):
    pass


class People(SingleValueSchema):
    pass


class Files(SingleValueSchema):
    pass


class CheckBox(SingleValueSchema): pass


class URL(SingleValueSchema): pass


class Email(SingleValueSchema): pass


class Phone(SingleValueSchema): pass


class Formula(Schema):
    def __init__(self, pname: str):
        super().__init__(pname)
        raise NotImplementedError()


class Relation(Schema):
    def __init__(self, pname: str):
        super().__init__(pname)
        raise NotImplementedError('Relation property is not supported currently.')


class Rollup(Schema):
    def __init__(self, pname: str):
        super().__init__(pname)
        raise NotImplementedError('Rollup property is not supported currently.')


class CreatedTime(SingleValueSchema):
    property_name = 'created_time'


class CreatedBy(SingleValueSchema):
    property_name = 'created_by'


class LastEditedTime(SingleValueSchema):
    property_name = 'last_edited_time'


class LastEditedBy(SingleValueSchema):
    property_name = 'last_edited_by'
