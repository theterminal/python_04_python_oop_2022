# Abstract Classes with ABC Module


"""
Abstract base classes (ABCs) enforce derived classes to implement particular methods from the base class.
    *) We implement it using the abc module.

"""


# --------- How NOT to do it ------------


class Shape:
    def __init__(self):
        if type(self) == Shape:
            raise Exception('…')

    def area(self):
        raise Exception('…')

    def perimeter(self):
        raise Exception('…')


# --------- The correct way --------------


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# ----------------------------------------
