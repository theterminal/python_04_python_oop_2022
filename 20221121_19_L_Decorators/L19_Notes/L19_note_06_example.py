# 20221121 - Python - Python OOP - Decorators
# Note 06 - Example Decorators


def multiply(n):                                        # outside function returns decorator
    def decorator(fun_ref):                             # decorator function returns wrapper
        def wrapper(*args):                             # wrapper function returns result
            result = fun_ref(*args)
            return result * n
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


@multiply(4)
def add(a, b):
    return a + b


print(add_ten(3))
print(add(15, 15))

