from fnmatch import fnmatch
from .registry import register,TaskBuilder,match_task
from ..task import Task

def build_task(task, name, g=None):
    assert isinstance(task, dict)
    builder=match_task(task)
    tasks = builder.build(task, name,g)
    if isinstance(tasks, Task):
        tasks = [tasks]
    return tasks

@register("task-group")
class TaskGroup(TaskBuilder):
    def match(self,task:dict):
        return "tasks" in task
    def build(self,cfg:dict, name, g=None, task_spec=None):
        '''
        task_spec example: 'train-*,test-*'
        '''
        if g is None:
            g = {}
        task_dict = cfg.get('tasks')
        # print(task_dict.keys())
        if isinstance(task_dict, (list, tuple, set)):
            task_dict = {str(k): v for k, v in enumerate(task_dict)}
        def search_keys(pattern, candidates):
            if not {',', '*'}.intersection(set(list(pattern))):
                if pattern in candidates:
                    # print(pattern)
                    return [pattern]
                else:
                    return None
            results = []
            if ',' in pattern:
                for p in pattern.split(','):
                    p = p.strip()
                    r = search_keys(p, candidates)
                    if r is not None:
                        results += r
            for cand in candidates:
                if fnmatch(cand, pattern) and not cand in results:
                    results.append(cand)
            return results

        if task_spec:
            keys = search_keys(str(task_spec), list(task_dict.keys()))
            task_dict = {key: task_dict[key] for key in keys}

        task_dict = {f'{name}-{key}': v for key, v in task_dict.items()}
        task_list = []
        for name, t in task_dict.items():
            # print(name)
            task_list += build_task(t, name, g)
        return task_list


