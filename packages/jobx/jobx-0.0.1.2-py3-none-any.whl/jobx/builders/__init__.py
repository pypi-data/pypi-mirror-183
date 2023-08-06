from .cmd import build_cmd_task
from .python import build_python_task
from .task_group import build_task_group
class Builder:
    @staticmethod
    def build(task, name,task_spec):
        return build_task_group(task, name,task_spec)



