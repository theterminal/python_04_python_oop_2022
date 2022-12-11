# 20221107 - Python - Python OOP
# Note 05 - Class Methods & Static Methods - Example 01
# The proper way to override using class methods


class Person:
    min_age = 0
    max_age = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def __validate_age(value):                                      # __validate_age() takes the class attributes of class Person
        if value < Person.min_age or value > Person.max_age:
            raise ValueError(f"The person's age must be between {Person.min_age} and {Person.max_age}")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value


class Employee(Person):                                              # __validate_age() takes the class attribute min_age of class Employee
    min_age = 16
    max_age = 77

    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = name
        self.age = age

    @staticmethod
    def __validate_age(value):
        if value < Employee.min_age or value > Employee.max_age:
            raise ValueError(f"The employee's age must be between {Employee.min_age} and {Employee.max_age}")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value


p_1 = Person('Jerry', 55)
print(p_1.name, p_1.age)

# p_2 = Person('George', 155)                                               # ValueError: 155 must be between 0 and 150
# print(p_2.name, p_2.age)

e_1 = Employee('Peter', 21)
print(e_1.name, e_1.age)

# e_2 = Employee('Gerhard', 12)                                             # ValueError: The age must be between 16 and 77
# print(e_2.name, e_2.age)
