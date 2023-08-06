import os
from jobx.utils import  generate_env_string
from jobx.task import Task

def build_cmd_task(task:dict, name):
        command = task['command']
        env = task.get('env',{})
        def task():
            os.system(generate_env_string(**env)+command)
        return Task(task, name)
