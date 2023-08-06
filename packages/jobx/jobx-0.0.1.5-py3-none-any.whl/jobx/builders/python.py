from jobx.utils import import_module, generate_env_string
from jobx.task import Task
import os
import sys
from .registry import register
@register("python")
def build_python_task(task:dict, name, g=None):
    python_file = task['path']
    args = task.get('args',[])
    kwargs = task.get('kwargs',{})
    func_name= task.get('function',None)
    env=task.get('env',{})
    if func_name:
        module = import_module(python_file)
        func = getattr(module, func_name)
        task = lambda: func(*args, **kwargs)
        return Task(task, name, g)
    else:
        args = ' '.join([str(x) for x in args])
        kwargs_str = []
        for k, v in kwargs.items():
            if isinstance(v, bool):
                if v:
                    kwargs_str.append('--%s' % (k))
                else:
                    continue
            else:
                kwargs_str.append('--%s=%s' % (k, v))
        kwargs = ' '.join(kwargs_str)

        def task():
            os.system(generate_env_string(**env)+f"{sys.executable} {python_file}{' ' + args if args else ''}{' ' + kwargs if kwargs else ''}")
        return Task(task, name)
