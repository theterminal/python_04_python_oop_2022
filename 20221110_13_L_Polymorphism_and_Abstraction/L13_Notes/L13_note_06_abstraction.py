# Abstraction


"""
In object-oriented programming, abstraction is one of the four central principles.
Through abstraction, we hide all but the relevant data about an object to reduce complexity and increase efficiency.

Abstraction can be achieved by:
    *) Functions and methods
    *) Abstract classes

Abstract classes are classes that contain one or more abstract methods.
    *) An abstract method is a method that is declared but contains no implementation.

Abstract classes may not be instantiated and require subclasses to provide implementations for the abstract methods.
"""

# ---------------------------------------------


# It could be achieved using exceptions, BUT IT IS NOT GOOD PRACTICE!


class Shape:
    def __init__(self):
        if type(self) is Shape:
            raise Exception('This is an abstract class')

    def area(self):
        raise Exception('This is an abstract class')

    def perimeter(self):
        raise Exception('This is an abstract class')
