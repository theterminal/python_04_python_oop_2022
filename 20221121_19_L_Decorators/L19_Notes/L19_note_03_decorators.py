# 20221121 - Python - Python OOP - Decorators
# Note 03 - Decorators


"""
Decorators are a very powerful and useful tool.
It allows programmers to modify the behavior of a function or a class.
Decorators allow us to wrap another function in order to extend the behavior of the wrapped function.
"""


# _________ Blueprint for Decorator creation ____________


def decorator_name(func_ref):                            # func_ref is the function above which the decorator is placed.
    def wrapper():
        pass

    return wrapper


# _________ Using Decorators ____________________________


"""
Our decorator function takes a function as an argument, so let us define a function and pass it to our decorator.
We learned earlier that we could assign a function to a variable.
We'll use that trick to call our decorator function.
"""


def say_hi():
    return 'hello there'


def uppercase_decorator():
    return say_hi().upper()


decorate = uppercase_decorator()
print(decorate)


"""
However, Python provides a much easier way for us to apply decorators.
We simply use the @ symbol before the function we would like to decorate.
"""


print('\n_____ example 1 _____ decorator uppercase _____ losing function name ______\n')


def uppercase(func_ref):
    def wrapper():
        return func_ref().upper()

    return wrapper


@uppercase
def say_hi():
    return 'Hello World!'


@uppercase
def say_bye():
    return 'Goodbye!'


print(say_hi())
print(say_bye())

print(say_bye.__name__)             # We are losing the original name of the function (was 'say_bye', now is 'wrapper')
print(say_hi.__name__)              # We are losing the original name of the function (was 'say_bye', now is 'wrapper')


"""
In the given example, if we try to call the name of the wrapped function the result is "wrapper", 
and its docstring is lost! See the example above.

To solve this problem, we use a decorator factory as a function decorator when defining a wrapper function.
"""


print('\n_____ example 2 _____ decorator uppercase _____ preserving function name ______\n')


from functools import wraps                     # must import it to use wraps


def uppercase(func_ref):
    @wraps(func_ref)                            # using @wraps(reference_to_the_function) to preserve the name of the function
    def wrapper():
        return func_ref().upper()

    return wrapper


@uppercase
def say_hi():
    return 'Hello World!'


@uppercase
def say_bye():
    return 'Goodbye!'


print(say_hi())
print(say_bye())

print(say_bye.__name__)             # We keep the original name of the function (was 'say_bye' and it is 'say_bye')
print(say_hi.__name__)              # We keep the original name of the function (was 'say_hi' and it is 'say_hi')
