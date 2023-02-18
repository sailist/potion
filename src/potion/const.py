default_headers = {
    'Content-Type': 'application/json',
    'Notion-Version': '2022-02-22'
}

current_headers = {}


class NotionHeader:
    def __init__(self, authorization, notion_version=None):
        self._headers = {
            'Authorization': authorization
        }
        if notion_version is not None:
            self._headers['Notion-Version'] = notion_version

    @property
    def headers(self) -> dict:
        val = {}
        val.update(default_headers)
        val.update(self._headers)
        return val

    # @contextmanager
    # def __call__(self):
    #     headers = {}
    #     headers.update(default_headers)
    #     headers['Authorization'] = self.authorization
    #     current_headers.update(headers)
    #     if self.notion_version is not None:
    #         headers['Notion-Version'] = self.notion_version
    #     try:
    #         yield headers
    #     finally:
    #         current_headers.clear()
