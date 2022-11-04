# 20221027 - Python OOP - Classes and Objects
# Methods __doc__, __dict__


print('\n--------------- __doc__ method --------------- \n')


class MyClass:
    """This is MyClass."""

    def example(self):
        """This is the example module of MyClass."""


print(MyClass.__doc__) # This is MyClass.
print(MyClass.example.__doc__)
# This is the example module of MyClass.


print('\n--------------- __dict__ method --------------- \n')


class MyClass:
    class_variable = 1

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable


first = MyClass(2)
second = MyClass(3)

print(MyClass.__dict__)   # {'__module__': '__main__', ... }
print(first.__dict__)     # { 'instance_variable': 2 }
print(second.__dict__)    # { 'instance_variable': 3 }


# -----------------------------------------------------------
