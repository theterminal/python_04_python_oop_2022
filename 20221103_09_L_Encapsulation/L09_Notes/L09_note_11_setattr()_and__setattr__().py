# 20221103 - Python - Python OOP - Encapsulation
# Note 11 - Function / method setattr() and __setattr__()


print('\n-------- setattr() -----------\n')


"""

setattr()

Used to set the value of the attribute. Returns 'None'
The method takes 3 parameters: Object, Name, Value

"""


class Person:
    def __init__(self, name):
        self.name = name


person = Person('Peter')
print(person.name)

print(setattr(person, 'name', 'George'))        # None
print(person.name)                              # George

print(setattr(person, 'age', 21))               # None
print(person.age)                               # 21

print(person.name, person.age)


print('\n-------- __setattr__() -----------\n')


"""

__setattr__()

Called when an attribute assignment is attempted

The method takes 2 parameters:
Name (of the attribute), Value (to assign to the attribute)

"""


class Phone:
    def __setattr__(self, attr, value):
        self.__dict__[attr] = value.upper()


phone = Phone()
phone.color = 'black'
print(phone.color)                              # BLACK
