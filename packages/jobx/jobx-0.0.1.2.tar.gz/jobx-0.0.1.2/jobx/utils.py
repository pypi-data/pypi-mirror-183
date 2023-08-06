import  os
import  platform

def import_module(python_file):
    import sys
    sys.path.append(os.getcwd())
    import importlib
    mod = importlib.import_module(convert_path_to_module_string(python_file))
    return mod

def get_platform():
    return platform.system().lower()
def generate_env_string(**kwargs):
    if get_platform()=='windows':
        return ' && '.join(['set %s=%s'%(k,v) for k,v in kwargs.items()])+( " && " if len(kwargs) else '')
    else:
        return ' '.join(['%s=%s'%(k,v) for k,v in kwargs.items()])+ ( "  " if len(kwargs) else '')

def load_json(f):
    import json
    with open(f, 'r', encoding='utf-8') as f:
        return json.load(f)

def convert_path_to_module_string(python_file):
    import os
    relpath = os.path.relpath(python_file, os.getcwd())

    def replace_all(s: str, args, target):
        for p in args:
            s = s.replace(p, target)
        return s

    def convert(relpath):
        return replace_all(relpath, ['./', '.\\'], '.').replace('/', '.').replace('\\', '.').replace('.py', '')

    return convert(relpath)


def dict2obj(dic):
    class C:
        pass

    o = C()
    for k, v in dic.items():
        setattr(o, k, v)
    return o
