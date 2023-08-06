from .cmd import build_cmd_task
from .python import build_python_task
from .task_group import build_task_group


builder_factory = {
    'python': build_python_task,
    'task-group': build_task_group,
    'cmd': build_cmd_task,
}
