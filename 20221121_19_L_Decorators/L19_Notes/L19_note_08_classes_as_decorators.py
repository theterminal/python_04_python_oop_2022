# 20221121 - Python - Python OOP - Decorators
# Note 08 - Classes as Decorators


"""
We can also use classes as decorators.
We usually do that when we need to maintain a state.
To use a class as a decorator, we need to implement the __call__ method.
The __call__ method allows class instances to be called as functions.
"""


# ________ example of calling a class as a function and returning error 'object NOT callable'________


class Fibonacci:
    def __init__(self):
        pass


f = Fibonacci()
# print(f())                                      # TypeError: 'Fibonacci' object is not callable


# ________ same example utilizing the __call__ method ______________


class Fibonacci:
    def __init__(self):
        self.nums = []

    def __call__(self, *args, **kwargs):
        return 'Hello World!'


f = Fibonacci()
print(f())                                      # Hello World!
