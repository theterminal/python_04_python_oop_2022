# 20221103 - Python - Python OOP - Encapsulation
# note 07 - Getters and Setters - Example


"""
You should use Python properties to apply rules to an attribute.
The property decorator is the pythonic way of using getters and setters.

Mainly setters and getters are used when data validation is needed!
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise Exception("Age must be greater than zero")
        self.__age = value
