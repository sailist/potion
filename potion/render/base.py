import json
import os
import re
from collections import defaultdict
import shutil
from typing import Union, List
from pathlib import Path
from potion.objects import NotionObject, Page, Database


class Parser:
    ext = '.json'

    def __init__(self, **kwargs):
        self._config = kwargs

    def parse(self, doc_info: Union[Page, Database], children=None):
        raise NotImplementedError()


match_invalid = re.compile('/')


def safe_path(title):
    return match_invalid.sub('_', title)


class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = set() if children is not None else children


class DocumentRelation:
    def __init__(self, documents: List[Union[Page, Database]], meta=None):
        self.meta = meta
        self.roots = set()
        self.tree = defaultdict(set)
        self.rev_tree = {}
        self.id_doc_map = {}

        for doc in documents:
            if doc.parent.type == 'workspace':
                self.root = doc
            else:
                pid = doc.parent[doc.parent.type]
                self.rev_tree[doc.id] = pid
                self.tree[pid].add(doc.id)

            self.id_doc_map[doc.id] = doc

        mem = set()
        node_index = {}

        for cid, pid in self.rev_tree.items():
            if pid not in self.rev_tree and pid in self.id_doc_map:
                self.roots.add(pid)

    def parse_org(self, parser: Parser, tgt_path: Path):
        for root_id in self.roots:
            self.parse_tree(parser, root_id, tgt_path)

    def parse_tree(self, p: Parser, cid, tgt_path: Path):
        os.makedirs(str(tgt_path), exist_ok=True)

        doc = self.id_doc_map[cid]
        title = f'{doc.string_title}_{doc.short_id}'

        children = self.tree[cid]
        content = p.parse(doc, children)

        tgt_file = tgt_path / safe_path(f'{title}.{p.ext}')
        try:
            tgt_file.write_text(content)
        except:
            print(tgt_file)

        # parse children
        for child in children:
            self.parse_tree(p, child, tgt_path)
