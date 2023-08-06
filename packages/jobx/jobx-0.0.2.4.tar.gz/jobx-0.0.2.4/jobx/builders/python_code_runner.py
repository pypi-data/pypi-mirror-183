from jobx.task import Task
import textwrap

from .registry import register,TaskBuilder
@register(["python-code","py-code"])
class PythonCodeRunner(TaskBuilder):
    def match(self,task:dict):
        return "python-code" in task or "py-code" in task
    def build(self,task:dict, name, g=None):
        code = task.get("py-code",task.get("python-code"))
        env = task.get('env',{})
        code=textwrap.dedent(code)
        def task():
            exec(code)
        return Task(task, name, g)

