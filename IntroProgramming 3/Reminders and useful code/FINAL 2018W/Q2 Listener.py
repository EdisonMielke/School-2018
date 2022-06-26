class Listener(object):

    def notify(self, event: dict):
        raise NotImplementedError("You most override notify")

class Listenable(object):

    def __init__(self):
        self.listeners = [ ]

    def add_listener(self, listener: Listener):
        self.listeners.append(listener)

    def notify_all(self, event: dict):
        for listener in self.listeners:
            listener.notify(event)

class SillyWalk(Listenable):
    def __init__(self, steps: list):
        super().__init__()
        self.steps = steps

    def walk(self):
        for step in self.steps:
            self.notify_all({ "step": step })

class StepWatcher(Listener):
    def __init__(self):
        self.count = 0

    def notify(self, event: dict):
        self.count += 1
        print("Step {}: {}".format(self.count, event["step"]))

silly = SillyWalk( ["kick", "wiggle", "swing"])
silly.add_listener(StepWatcher())
silly.walk()