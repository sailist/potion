# b'{"object":"error","status":401,"code":"unauthorized","message":"API token is invalid."}'
from .common import NotionObject


class Error(NotionObject):
    def __init__(self, status: int, code: str, message: str, object=None):
        super().__init__(None, kwargs=dict(status=status, code=code, message=message))
