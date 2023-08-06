import os
from jobx.utils import  generate_env_string
from jobx.task import Task

from .registry import register,TaskBuilder
@register(["command","cmd"])
class Command(TaskBuilder):
    def match(self,task:dict):
        return "cmd" in task or "command" in task
    def build(self,task:dict, name, g=None):
        command = task.get("cmd",task.get("command"))
        env = task.get('env',{})
        def task():
            os.system(generate_env_string(**env)+command)
        return Task(task, name, g)

