import  time

class Task:
    def __init__(self, target, name) -> None:
        self.target = target
        self.started = False
        self.finished = False
        self.name = name
        self.on_started = None
        self.on_finished = None

    def set_on_started(self, func):
        self.on_started = func

    def set_on_finished(self, func):
        self.on_finished = func

    def start(self):
        self.started = True
        if self.on_started:
            self.on_started(self)
        start_time = time.time()
        print(("Task %s started." % (self.name)).center(100, "="))
        self.target()
        end_time = time.time()
        print(("Task %s finished. Time used: %.5f" % (self.name, end_time - start_time)).center(100, "="))
        if self.on_finished:
            self.on_finished(self)
        self.finished = True

