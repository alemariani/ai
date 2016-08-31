import threading

class IO (threading.Thread):
    def __init__(self, brain):
        threading.Thread.__init__(self)
        self.brain = brain
