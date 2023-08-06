from jobx.task import Task
from .registry import builder_factory
def build_task(task, name):
    assert isinstance(task, dict)
    task_type = task.get('type', 'python')
    tasks = builder_factory[task_type](task, name)
    if isinstance(tasks, Task):
        tasks = [tasks]
    return tasks

