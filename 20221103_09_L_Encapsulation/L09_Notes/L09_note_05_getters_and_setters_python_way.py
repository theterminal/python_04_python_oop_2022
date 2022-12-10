# 20221103 - Python - Python OOP - Encapsulation
# Note 05 - Getters and Setters


"""

The "pythonic" way of defining getters and setters is using properties.
By defining properties, you can change the internal implementation of a class without affecting the program.

Mainly setters and getters are used when data validation is needed!

If an instance attribute has a getter and setter (properties), before the value is assigned in the init it
will go to the properties and will check the conditions and after that will set it if value meets the conditions
set in the setter.

"""


class Person:
    def __init__(self, age=0):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 18:
            self.__age = 18
        else:
            self.__age = age


person = Person(25)
print(person.age)                           # 25

person.age = 10
print(person.age)                           # 18
