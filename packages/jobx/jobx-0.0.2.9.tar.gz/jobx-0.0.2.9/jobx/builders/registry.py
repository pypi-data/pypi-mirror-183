from typing import Dict

class TaskBuilder:
    type=None
    def build(self,task:dict, name, g=None):
        raise NotImplementedError()
    def match(self,task:dict):
        return self.type and task.get("type")==self.type

builder_factory:Dict[str,TaskBuilder] = {}
builders=[]



def match_task(task)->TaskBuilder:
    task_type = task.get('type',None)
    if task_type:
        return builder_factory[task_type]
    for tp,builder in builder_factory.items():
        if builder.match(task):
            return builder

def register(names):
    if isinstance(names,str):
        names=[names]
    def decorator(plugin):
        assert  issubclass(plugin,TaskBuilder)
        builder=plugin()
        for name in names:
            builder_factory[name]=builder
        builders.append(builder)
        return plugin
    return decorator
