from fnmatch import fnmatch
from .task import build_task
from .registry import register

@register("task-group")
def build_task_group(cfg, name, task_spec=None):
    '''
    task_spec example: 'train-*,test-*'
    '''
    task_dict = cfg.get('tasks')
    # print(task_dict.keys())
    if isinstance(task_dict, (list, tuple, set)):
        task_dict = {str(k): v for k, v in enumerate(task_dict)}
    def search_keys(pattern, candidates):
        if not set([',', '*']).intersection(set(list(pattern))):
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
        task_list += build_task(t, name)
    return task_list

