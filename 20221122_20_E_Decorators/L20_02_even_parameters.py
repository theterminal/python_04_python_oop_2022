# 20221122 - Python - Python OOP - Decorators
# 02 - Even Parameters - judge url: https://judge.softuni.org/Contests/Compete/Index/1947#1


from functools import wraps


def even_parameters(func):                          # func is a referring to 'add' function
    @wraps(even_parameters)
    def wrapper(*args):
        for arg in args:
            if isinstance(arg, int):
                if arg % 2 == 0:
                    continue
            return 'Please use only even numbers!'
        return func(*args)
    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
