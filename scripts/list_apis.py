from potion.api import *
from potion.objects import *
import inspect


def main():
    api_dic = {

    }

    api_items = []

    for k, v in list(globals().items()):
        if not k.startswith('_'):
            if not inspect.ismodule(v):
                api_items.append([k, v])
            else:
                for member in inspect.getmembers(v):
                    kk, vv = member
                    api_items.append([kk, vv])

    for k, v in api_items:
        if not k.startswith('_'):
            m = inspect.getmodule(v)
            if m is not None and m.__name__.startswith('potion'):
                api_dic.setdefault(m.__name__, set()).add(k)

    with open('../api.md', 'w') as w:
        for k, v in sorted(api_dic.items()):
            path = k.replace('.', '/')
            w.write(f"[{k}](./{path}.py)\n")
            for vv in sorted(v):
                w.write(f' - {vv}\n')
            w.write('\n')


if __name__ == '__main__':
    main()
