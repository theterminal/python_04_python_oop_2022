# 20221121 - Python - Python OOP - Decorators
# Note 05 - Passing Arguments to Decorators


"""
So far we've worked with only one parameter passed to the decorator.
So, decorators that expect arguments...

It is a function that returns a decorator...

In order to achieve this, we define a decorator maker that accepts arguments.
Then we define a decorator inside it.
We then define a wrapper function inside the decorator as we did earlier.
"""


from functools import wraps


def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(4)
def say_hi():
    print("Hello")


print(say_hi.__name__)                      # check for name of the func

if __name__ == '__main__':
    say_hi()
