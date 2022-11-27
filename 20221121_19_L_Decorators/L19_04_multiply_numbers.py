# 20221121 - Python - Python OOP - Decorators
# 04 - Multiply Numbers - judge url: https://judge.softuni.org/Contests/Practice/Index/1946#3


def multiply(n):
    def decorator(fun_ref):
        def wrapper(*args):
            result = fun_ref(*args)
            return result * n
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
