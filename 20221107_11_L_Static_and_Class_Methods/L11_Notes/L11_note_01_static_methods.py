# 20221107 - Python - Python OOP
# Note 01 - Static Methods


"""

It knows nothing about the class or instance it is called on.
It cannot modify object state or class state.
It could be put outside the class, but it is inside the class where it is applicable.
To turn a method into a static, a line with @staticmethod in front of the method header must be added.

To call a static method, both, the instance or the class can be used.

Benefits:
--------
Shows that a particular method is independent of everything else around it.
Often helps to avoid accidentals modifications that go against the original design.
Communicates and enforces developer intent about the class design.
It is much easier to test since it is completely independent of the rest of the class.

"""


class Person:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def is_adult(age):
        return age >= 18


print(Person.is_adult(5))           # False
girl = Person("Amy")
print(girl.is_adult(20))            # True
