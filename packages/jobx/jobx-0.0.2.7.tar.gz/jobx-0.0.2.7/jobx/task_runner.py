from .task import Task
import  time
import threading

class BatchTaskRunner:
    def __init__(self, tasks, workers_limit=5, delay=0, silent=False) -> None:
        self.tasks = tasks
        self.workers_limit = workers_limit
        self.running_workers = 0
        self.delay = delay
        self.silent=silent
        for task in self.tasks:
            assert isinstance(task, Task)
            # task.set_on_started(self.on_task_started)
            task.set_on_finished(self.on_task_finished)

    def on_task_started(self, task: Task):
        self.running_workers += 1

    def on_task_finished(self, task: Task):
        self.running_workers -= 1

    def get_one(self):
        for task in self.tasks:
            if not task.started:
                return task
        return None

    def start_task(self, task):
        self.on_task_started(task)
        thread = threading.Thread(target=task.start)
        thread.start()

    def all_task_finished(self):
        for task in self.tasks:
            if not task.finished:
                return False
        return True

    def exit(self):
        if not self.silent:
            print("All task finished".center(100, "="))

    def run(self):
        if not self.silent:
            print(f"Going to run {len(self.tasks)} tasks.".center(100,"="))
        while True:
            if self.all_task_finished():
                break
            while self.running_workers < self.workers_limit:
                task = self.get_one()
                if not task:
                    break
                self.start_task(task)
                time.sleep(self.delay)
            time.sleep(0.1)
        self.exit()
