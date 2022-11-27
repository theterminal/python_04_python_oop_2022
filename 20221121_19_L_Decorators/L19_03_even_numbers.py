# 20221121 - Python - Python OOP - Decorators
# 03 - Even Numbers - judge url: https://judge.softuni.org/Contests/Practice/Index/1946#2


from functools import wraps


def even_numbers(func_ref):
    @wraps(func_ref)
    def wrapper(*args):
        result = func_ref(*args)
        return [x for x in result if x % 2 == 0]

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 12]))
