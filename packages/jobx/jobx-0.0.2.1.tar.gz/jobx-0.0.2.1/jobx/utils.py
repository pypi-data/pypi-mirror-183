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

class EasyDict(dict):
  def __init__(self, **kwargs):
    d = {}
    if kwargs:
      d.update(**kwargs)
    for k, v in d.items():
      setattr(self, k, v)
    # Class attributes
    for k in self.__class__.__dict__.keys():
      if not (k.startswith('__') and k.endswith('__')) and not k in ('update', 'pop'):
        setattr(self, k, getattr(self, k))

  def __setattr__(self, name, value):
    if isinstance(value, (list, tuple)):
      value = [self.__class__(x)
      if isinstance(x, dict) else x for x in value]
    elif isinstance(value, dict) and not isinstance(value, self.__class__):
      value = self.__class__(**value)
    super(EasyDict, self).__setattr__(name, value)
    super(EasyDict, self).__setitem__(name, value)
  __setitem__ = __setattr__


  def update(self, e=None, **f):
    d = e or dict()
    d.update(f)
    for k in d:
      setattr(self, k, d[k])

  def pop(self, k, d=None):
    delattr(self, k)
    return super(EasyDict, self).pop(k, d)



def deepmerge(a,b,path=None):
    "merges b into a"
    if path is None: path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                deepmerge(a[key], b[key], path + [str(key)])
            elif a[key] == b[key]:
                pass # same leaf value
            else:
                raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
        else:
            a[key] = b[key]
    return a
