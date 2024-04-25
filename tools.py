import timeit

class Timer:
    def __init__(self):
        self.start_time = 0.0
        self.stop_time = 0.0

    def start(self):
        self.start_time = timeit.default_timer()

    def stop(self):
        self.stop_time = timeit.default_timer()

    def get_time(self) -> float:
        return self.stop_time - self.start_time
