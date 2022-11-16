# 20221107 - Python - Python OOP
# Note 05 - Class Methods & Static Methods - Example 02


# the proper way to override using class methods


class Person:
    MIN_AGE = 0
    MAX_AGE = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def __validate_age(cls, value):                                        # __validate_age() takes the class attributes of class Person
        if value < Person.MIN_AGE or value > Person.MAX_AGE:
            raise ValueError(f'{value} must be between {cls.MIN_AGE} and {cls.MAX_AGE}')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value


class Employee(Person):                                                     # __validate_age() takes the class attribute min_age of class Employee
    MIN_AGE = 16

    def __init__(self, name, age, salary):
        super().__init__(name, age)                                         # when checking the age of the Employee
        self.salary = salary


p_1 = Person('Jerry', 55)
# p_2 = Person('George', 155)

e_1 = Employee('Peter', 21, 1000)
e_2 = Employee('Gerhard', 12, 500)
