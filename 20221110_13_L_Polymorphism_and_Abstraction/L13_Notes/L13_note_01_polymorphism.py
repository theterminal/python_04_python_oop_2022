# 20221110 - Python - Python OOP
# Note 1 - Example of runtime polymorphism. In Python there is NO compile-time polymorphism.


"""

Polymorphism is mostly pointed at functionality (methods) and not toward class attributes! It looks the same...
The names of the methods must be the same in order to talk about polymorphism.
Abstract methods is type of polymorphism but it is different.
In essence polymorphism is the possibility for the base class and all children classes to have different actions with one and the same method!
To expend on it, if you have different classes with same functionalities - that is NOT polymorphism.
Decorator is a function that works before the function you are calling.

Without polymorphism, we should implement check of the figure before calculations...

"""


class Shape:
    def calculate_area(self):
        return None


class Square(Shape):
    side_length = 2

    def calculate_area(self):
        return self.side_length * 2


class Triangle(Shape):
    base_length = 4
    height = 3

    def calculate_area(self):
        return 0.5 * self.base_length * self.height


a = Shape()
print(a)

b = Square()
print(b)
print(b.calculate_area())

c = Triangle()
print(c)
print(c.calculate_area())
