An object-oriented wrapper for Notion pages and database

```python
from potion.beans import NotionPage

page = NotionPage.create_from_parent()
page = NotionPage.retrieve_from_id()

page.set_property()
page.set_xxx()

with page.code_block('name') as b:
    b.code = ''
    b.language = ''
    b.caption = ''

with page.file_block() as f:
    f.file = ''

page.flush()
```

```python
from potion.beans import NotionDatabase
from potion.objects import Parent

database = NotionDatabase.create_from_parent(parent=Parent.PageParent(''))
database = NotionDatabase.retrieve_from_id()

database.update_property()
database.remove_property()
database.insert_property()

with database.page() as p:
    pass

database.flush()
```