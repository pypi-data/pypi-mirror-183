from .builders.task_group import TaskGroup
def build(task, name,task_spec):
    g=task
    return TaskGroup().build(task, name,g=g, task_spec=task_spec)

