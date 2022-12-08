# 20221027 - Python OOP - Classes and Objects
# Note 03 - Method __doc__


class MyClass:
    """This is MyClass."""

    def example(self):
        """This is the example module of MyClass."""


print(MyClass.__doc__)                                          # This is MyClass.
print(MyClass.example.__doc__)                                  # This is the example module of MyClass.
