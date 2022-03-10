# Potion

A functional, easy to use Python wrapper of Notion Api.

# Install

```shell
pip install py-notion
```

# Usage

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

- [ ] Filter Object Enums
- [ ] Parse json responses recurrsive into notion objects.

# Related

- [notion-py](https://github.com/jamalex/notion-py)