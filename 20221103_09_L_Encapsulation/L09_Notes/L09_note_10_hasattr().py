# 20221103 - Python - Python OOP - Encapsulation
# note 10 - Function / Method hasattr()


"""
hasattr()

Checks if an attribute exists or not.
Returns 'True' if an object has the given named attribute and 'False' if it does not

hasattr() takes 2 parameters: Object, Name
"""


class Person:
    def __init__(self, name):
        self.name = name


person = Person('Peter')
print(hasattr(person, 'name'))          # True
print(hasattr(person, 'age'))           # False
