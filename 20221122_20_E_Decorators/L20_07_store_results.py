# 20221122 - Python - Python OOP - Decorators
# 07 - *Store Results


class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        with open("results_l20_07.txt", "a") as result_file:
            result_file.write(f"Function '{self.func.__name__}' was add called. Result: {self.func(*args)}\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
