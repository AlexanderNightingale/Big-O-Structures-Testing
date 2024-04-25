import matplotlib.pyplot as plt
from random import randint
import array
from tools import Timer



def foo() -> float:
    timer = Timer()
    timer.start()
    timer.stop()
    return timer.get_time()


if __name__ == '__main__':

    time_all = 0.0
    REPEATS = 1_000

    for i in range(REPEATS):
        t = foo()*1_000_000
        time_all += t

    print(f"Time:{time_all/REPEATS}")

