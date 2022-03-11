import json
from typing import Dict, Union

import requests

from potion.objects import NotionObject
from .parser import parse


class Request:
    def __init__(self, headers=None):
        if headers is None:
            from potion.const import current_headers
            headers = current_headers
        assert 'Authorization' in headers
        self.headers = headers

    def get(self, url):
        content = json.loads(requests.get(url, headers=self.headers).content)
        return parse(dic=content)

    def post(self, url, data: Union[NotionObject, Dict, str]):
        if issubclass(data.__class__, NotionObject):
            data = data.to_json()
        content = json.loads(requests.post(url=url, data=data.encode(), headers=self.headers).content)
        return parse(dic=content)

    def patch(self, url, data: Union[NotionObject, Dict, str]):
        if issubclass(data.__class__, NotionObject):
            data = data.to_json()
        content = json.loads(requests.patch(url=url, data=data.encode(), headers=self.headers).content)
        return parse(dic=content)

    def delete(self, url):
        content = json.loads(requests.delete(url, headers=self.headers).content)
        return parse(dic=content)

    def parse(self):
        pass

    @staticmethod
    def from_token(authorization):
        from potion.const import NotionHeader
        nh = NotionHeader(authorization=authorization)
        return Request(nh.headers)
