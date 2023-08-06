import os
from jobx.utils import  generate_env_string
from jobx.task import Task

from .registry import register
@register("cmd")
def build_cmd_task(task:dict, name, g=None):
        command = task.get("cmd",task.get("command"))
        env = task.get('env',{})
        def task():
            os.system(generate_env_string(**env)+command)
        return Task(task, name, g)
