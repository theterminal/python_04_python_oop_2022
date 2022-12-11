# 20221107 - Python - Python OOP
# Note 04 - Overriding Using Methods


class Person:
    min_age = 0
    max_age = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # _________ block 1 start ___________
    @staticmethod
    def __validate_age(value):
        if value < Person.min_age or value > Person.max_age:
            raise ValueError()

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value
    # _________ block 1 end ___________


class Employee(Person):
    min_age = 16
    max_age = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __________ block 2 start ___________ overrides all methods bellow compared with block 1 _____________
    @staticmethod
    def __validate_age(value):
        if value < Employee.min_age or \
           value > Employee.max_age:
            raise ValueError()

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value
    # _________ block 2 end ___________
