# 20221122 - Python - Python OOP - Decorators
# 05 - Cache - judge url: https://judge.softuni.org/Contests/Compete/Index/1947#4


def cache(func):
    def wrapper(num):
        if num not in wrapper.log:
            wrapper.log[num] = func(num)
        return wrapper.log[num]
    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# ______________ Test Code 1 ______________


fibonacci(3)
print(fibonacci.log)


# ______________ Test Code 2 ______________


fibonacci(4)
print(fibonacci.log)
