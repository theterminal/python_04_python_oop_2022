# 20221121 - Python - Python OOP - Decorators
# Note 07 - Decorating Methods in Classes


"""
@classmethod            - decorator function that converts a method to a class method
@abstractmethod         - decorator function that converts an instance method to an abstract instance method
@abstractclassmethod    - decorator function that converts a class method to an abstract class method
@property               - change your class methods/attributes so that the user of a class doesn't need to make any change in their code
"""


# Example: property decorator


class Person:
    def __init__(self):
        self.__name = ''

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
