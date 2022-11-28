# 20221122 - Python - Python OOP - Decorators
# 01 - Logged - judge url: https://judge.softuni.org/Contests/Compete/Index/1947#0


def logged(function):
    def wrapper(*args):
        return f'you called {function.__name__}({", ".join(str(arg) for arg in args)})\nit returned {function(*args)}'
    return wrapper


# __________________ Test Code 1 ___________________


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


# __________________ Test Code 2 ___________________


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
