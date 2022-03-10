from typing import List, Dict, Tuple
import json


class _Null: pass


Null = _Null()


class NotionObject:
    property_name = None
    union_type = 'list'
    include_type = False

    def __init__(self, pname: str, args=None, kwargs=None):
        self._name = pname
        if args is not None:
            self._value = args
        elif kwargs is not None:
            self._value = {k: v for k, v in kwargs.items() if v is not None}
        else:
            self._value = {}

    def __getitem__(self, item):
        if isinstance(self._value, dict):
            return self._value.get(item, None)
        elif isinstance(item, int) and isinstance(self._value, list):
            return self._value[item]
        raise NotImplementedError()

    def __repr__(self):
        return self.to_json(indent=2)

    @property
    def prop(self):
        if self.property_name is None:
            return self.__class__.__name__.lower()
        return self.property_name

    def to_dict(self):
        if isinstance(self._value, _Null):
            return {
                self._name: None
            }

        values = recur_to_dict(self._value)
        if self.union_type == 'dict' and isinstance(values, list):
            _v = {}
            [_v.update(i) for i in values]
            values = _v

        if self._name is None:
            return values

        if self._name == '':
            return {
                self.prop: values
            }

        val = {}
        if self.include_type:
            val['type'] = self.prop
        val[self.prop] = values

        return {
            self._name: val
        }

    def to_json(self, indent=0):
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=indent)

    def parse_schema(self, name, dic: dict):
        """
        parse_schema(k,v) for k,v in properties.items()
        :param name:
        :param dic:
        :return:
        """


class Parent(NotionObject):
    def __init__(self, type=None, page_id=None, workspace: bool = None, database_id=None):
        super().__init__(None, kwargs=dict(type=type, page_id=page_id,
                                           workspace=workspace, database_id=database_id))

    @staticmethod
    def PageParent(page_id):
        return Parent(type='page_id', page_id=page_id)

    @staticmethod
    def DataBaseParent(database_id):
        return Parent(database_id=database_id)

    @staticmethod
    def PageWorkspaceParent():
        return Parent(type='workspace', workspace=True)


class Properties(NotionObject):
    union_type = 'dict'

    def __init__(self, *property: NotionObject):
        super().__init__(None, args=property)

    @staticmethod
    def from_dict(dic):
        return Properties(dic)


class Any(NotionObject):
    def __init__(self, pname: str, property_name=None, union_type='list', include_type=False, args=None, kwargs=None):
        self.property_name = property_name
        self.union_type = union_type
        self.include_type = include_type
        super().__init__(pname, args=args, kwargs=kwargs)


def recur_to_dict(object):
    if isinstance(object, (List, Tuple)):
        return [recur_to_dict(i) for i in object]
    elif isinstance(object, Dict):
        return {k: recur_to_dict(v) for k, v in object.items()}
    elif isinstance(object, NotionObject):
        return object.to_dict()
    return object
