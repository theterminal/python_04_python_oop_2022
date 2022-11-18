# 20221110 - Python - Python OOP - Polymorphism and Abstraction
# 04 - Shapes - judge url: https://judge.softuni.org/Contests/Practice/Index/1942#2


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__()
        self.__radius = radius

    def calculate_area(self):
        return self.__radius * self.__radius * pi

    def calculate_perimeter(self):
        return 2 * pi * self.__radius


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return 2 * (self.__width + self.__height)


print('\n_______________ Test Code 1 ________________\n')


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())


print('\n_______________ Test Code 2 ________________\n')


rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())


print('\n____________ Another Way of combining both results _____________\n')


circle = Circle(5)
rectangle = Rectangle(10, 20)

for obj in [circle, rectangle]:
    print(obj.calculate_area())
    print(obj.calculate_perimeter())
