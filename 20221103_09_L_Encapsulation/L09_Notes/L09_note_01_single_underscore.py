# 20221103 - Python - Python OOP
# note 01 - Single Underscore (NON-PUBLIC method / variable)


"""
Using a single leading underscore is just a convention.
A name prefixed with an underscore should be treated as a 'non-public' method / variable
"""


class Person:
    def __init__(self, name, age=0):
        self.name = name
        self._age = age


person = Person('Peter', 25)
print(person.name)  # Peter
print(person._age)  # 25
