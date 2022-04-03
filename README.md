# Potion

A functional, easy to use Python wrapper of Notion Api.

- easy-to-use low-level api
- integration local-backup function
- [ ] render notion object to markdown/html, etc..

# Install

```shell
pip install notion-potion
```

# Usage

## Quick Start

Authentication

```python
from potion import Request, NotionHeader

token = ''

nh = NotionHeader(authorization=token)
req = Request(nh.headers)
```

> Create an integration follow [this official tutorial](https://developers.notion.com/docs/getting-started) to get `token`.

A 'retrieve' example. (Full code can be found [here](./examples/basic/database_retrieve.py))

```python
from potion.api import *

print(req.get(url=database_retrieve('1bb0f79b87584afe8609d6e248285cfb')))
```

And a 'update' example. ([Full code](./examples/basic/database_create.py))

```python
from potion.api import *
from potion.objects import *

property_list = [
    sche.AnySchema('+1', args=Null),  # delete property
    sche.URL('Photo'),  # update property type of `Photo`
    sche.MultiSelect('Store availability', [  # update Options of MultiSelect perproty `Store availability`
        sche.Option('Duc Loi Market'),
        sche.Option('Rainbow Grocery'),
        sche.Option('Gus\'s Community Market'),
        sche.Option('The Good Life Grocery', color='orange'),
    ])
]
properties = Properties(*property_list)

# Create Database object
data = Database(properties=properties)

# Commit update operation
print(data)
print(req.patch(url=database_update('1bb0f79b87584afe8609d6e248285cfb'),
                data=data))

```

## Basic Example

Here lists examples reimplemented by potion from [official shell examples](https://developers.notion.com/reference)

|Database|Pages|Blocks|Users|Search|
|---|---|---|---|---|
|[Query a Database](./examples/basic/database_query.py)|[Retrieve a page](./examples/basic/page_retrieve.py)|[Retrieve a block](./examples/basic/block_retrieve.py)|[Retrieve a user/List all users/Retrieve your token's bot user](./examples/basic/user_retrieve.py)|[Search](./examples/basic/search.py)|
|[Create a database](./examples/basic/database_create.py)|[Create a page](./examples/basic/page_create.py)|[Update a block](./examples/basic/block_update.py)|||
|[Retrieve a database](./examples/basic/database_retrieve.py)|[Update page](./examples/basic/page_update.py)|[Retrieve block children](./examples/basic/block_children_retrieve.py)|||
|[Update database](./examples/basic/database_update.py)|[Retrieve a page property item](./examples/basic/page_property_retrieve.py)|[Append block children](./examples/basic/block_append.py)|||
|||[Delete a block](./examples/basic/block_delete.py)|||
||||||

## Object Oriented Api

potion also provides object oriented operations for Notion page and Notion database:

```python
from potion.beans import NotionPage, NotionDatabase

token = ''
# Retrieve
page = NotionPage(auth=token, id=...)
# Create a new one
page = NotionPage(auth=token, parent=...)
print(page)

# set property
page.set_text('title', 'temp')
page.set_number('End', 42)
page.flush_property()

# append content
page.append_code("""print('hello world!')""", 'python')
page.flush_children()

# page.parent
## page.parent_database
## page.parent_page
database = page.create_database()
# TODO
# database operations
database.add_property()
database.update_property()
database.create_page()
```

## Backup

```shell
python -m potion.backup {token} {backup_dir}
# python -m potion.backup secret_umqPgKzCvvCaAc1FE408aRvYHymxaak5HriWIvaVzs ./backup
```

> It will use [dbrecord](https://github.com/sailist/dbrecord) to generate two sqlite database file under `backup_dir`.

You can read backuped data simpily by using the code below:

```python
from dbrecord import PList

backup_dir = ...
lis = PList(f'{backup_dir}/notion-backup.sqlite')
print(lis[0])
```

# Api List

See [api.md](./api.md) for details.

# Development & Contribute

```shell
git clone https://github.com/sailist/potion
python setup
```

Any issue and pr is welcome.

# TODOs

- [ ] Some uncommon used Object, like Filter, Emoji, File, etc..(While, you can implement your idea without this Object
  by pass dict as args.)
- [ ] Parse json responses recurrsive into notion objects.

# Related

- [notion-py](https://github.com/jamalex/notion-py)
- [dbrecord](https://github.com/sailist/dbrecord)