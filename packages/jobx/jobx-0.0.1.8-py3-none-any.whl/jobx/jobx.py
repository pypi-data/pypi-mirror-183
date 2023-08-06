import importlib
from .utils import convert_path_to_module_string,dict2obj,EasyDict
from .builders import Builder
from .task_runner import BatchTaskRunner
from .config import load_config
import os


def feed_func(python_file: str, func: str, *config_files: str, as_object=False, **kwargs):
    import sys
    sys.path.append(os.getcwd())
    import importlib
    mod = importlib.import_module(convert_path_to_module_string(python_file))
    params = {}
    for file in config_files:
        params.update(load_config(file))
    params.update(kwargs)
    if as_object:
        return getattr(mod, func)(dict2obj(params))
    else:
        return getattr(mod, func)(**params)


def feed(python_file: str, *config_files: str, **kwargs):
    import sys
    sys.path.append(os.getcwd())
    params = {}
    for file in config_files:
        params.update(load_config(file))
    params.update(kwargs)
    args = []
    for k, v in params.items():
        args.append('--%s=%s' % (k, v))
    args = ' '.join(args)
    os.system(' '.join([sys.executable, python_file, args]))

def run_tasks(task=None, **kwargs):
    config_file=kwargs.get("f",None) or kwargs.get("file","jobx.yaml")
    if "f" in kwargs:
        kwargs.pop("f")
    if "file" in kwargs:
        kwargs.pop("file")
    default_config=dict(
        workers_limit=1,
        delay=0,
        name="task",
        timer=False,
        silent=True
    )

    cfg = load_config(config_file, **kwargs)
    cfg.update(default_config)

    workers_limit = cfg.get('workers_limit', 1)
    delay = cfg.get('delay', 0)
    silent=cfg.get("silent",True)
    tasks = Builder.build(cfg, cfg.get('name', 'Task'), task)
    BatchTaskRunner(tasks, workers_limit, delay,silent=silent).run()


def job(job_name, *args, **kwargs):
    job_spec = job_name.split('.')
    module = importlib.import_module('.' + job_spec[0], 'jobs')
    jo = module
    for spec in job_spec[1:]:
        jo = getattr(jo, spec)
    jo(*args, **kwargs)


class CLI:
    feed_func = staticmethod(feed_func)
    feed = staticmethod(feed)
    tasks = staticmethod(run_tasks)
    run_tasks = staticmethod(run_tasks)
    job = staticmethod(job)


