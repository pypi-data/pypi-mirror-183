from jobx.task import Task
from .registry import builder_factory
def build_task(task, name, g=None):
    assert isinstance(task, dict)
    task_type = task.get('type', 'python')
    tasks = builder_factory[task_type](task, name,g)
    if isinstance(tasks, Task):
        tasks = [tasks]
    return tasks

