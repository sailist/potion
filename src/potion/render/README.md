# Documentation Relationship

Each rendered Notion page and database is a single markdown file. And the files will be organised as follow rules:

- A page linked in a parent page will be written in a subdirectory which has the same basename of the parent page
- A database under the parent page will be written in the same directory as the parent page and adding the parent page
  name as prefix.

Noticed that a page will have several subpage or subdatabase, but a database can only have page as children node, so
there are only three patterns we need to process, and I list these patterns below:

`Page -> Page -> Page`

```
{page_title}_{id[:4]}.md
{page_title}_{id[:4]}/{page_title}_{id[:4]}.md
{page_title}_{id[:4]}/{page_title}_{id[:4]}/{page_title}_{id[:4]}.md
```

`Page -> Database -> Page`

```
{page_title}_{id[:4]}.md
{page_title}_{id[:4]}.md.{sub_database}_{id[:4]}.md
{page_title}_{id[:4]}.md.{sub_database}_{id[:4]}/{sub_database_page_title}_{id[:4]}.md
```

`Database -> Page -> Any`

```
{database}_{id[:4]}.md
{database}_{id[:4]}/{sub_path_title}_{id[:4]}.md
```
