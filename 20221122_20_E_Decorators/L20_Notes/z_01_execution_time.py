# 20221122 - Python - Python OOP - Decorators
# 08 - *Execution Time


import time


def exec_time(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        return end - start

    return wrapper


@exec_time                                  # Calculates needed time for the execution
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10_000_000))
