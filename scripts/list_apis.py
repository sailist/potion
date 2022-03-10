from potion.api import *
import inspect

api_dic = {

}

for k, v in list(locals().items()):
    if not k.startswith('__'):
        m = inspect.getmodule(v)
        if m is not None and m.__name__.startswith('potion'):
            api_dic.setdefault(m.__name__, []).append(k)

with open('../api.md', 'w') as w:
    for k, v in sorted(api_dic.items()):
        path = k.replace('.', '/')
        w.write(f"[{k}](./{path}.py)\n")
        for vv in v:
            w.write(f' - {vv}\n')
        w.write('\n')
