import  time

class Task:
    def __init__(self, target, name, g=None) -> None:
        if g is None:
            g={}
        self.target = target
        self.started = False
        self.finished = False
        self.name = name
        self.g=g
        self.on_started = None
        self.on_finished = None

    def set_on_started(self, func):
        self.on_started = func

    def set_on_finished(self, func):
        self.on_finished = func

    def start(self):
        g=self.g
        self.started = True
        if self.on_started:
            self.on_started(self)
        if g.get("timer", False):
            start_time = time.time()
            print(("Task %s started." % (self.name)).center(100, "="))
        self.target()
        if g.get("timer", False):
            end_time = time.time()
            print(("Task %s finished. Time used: %.5f" % (self.name, end_time - start_time)).center(100, "="))
        if self.on_finished:
            self.on_finished(self)
        self.finished = True

