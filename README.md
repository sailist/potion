# Potion

A functional, easy to use Python wrapper of Notion Api.

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

### Database

- [Query a Database](./examples/basic/database_query.py)
- [Create a database](./examples/basic/database_create.py)
- [Retrieve a database](./examples/basic/database_retrieve.py)
- [Update database](./examples/basic/database_update.py)

### Pages

- [Retrieve a page](./examples/basic/page_retrieve.py)
- [Create a page](./examples/basic/page_create.py)
- [Update page](./examples/basic/page_update.py)
- [Retrieve a page property item](./examples/basic/page_property_retrieve.py)

### Blocks

- [Retrieve a block](./examples/basic/block_retrieve.py)
- [Update a block](./examples/basic/block_update.py)
- [Retrieve block children](./examples/basic/block_children_retrieve.py)
- [Append block children](./examples/basic/block_append.py)
- [Delete a block](./examples/basic/block_delete.py)

### Users

- [Retrieve a user/List all users/Retrieve your token's bot user](./examples/basic/user_retrieve.py)

### Search

- [Search](./examples/basic/search.py)

# Api

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