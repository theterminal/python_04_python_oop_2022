# 20221103 - Python - Python OOP - Encapsulation
# note 12 - Function delattr() and __delatrr__()


print('\n_________ delattr() _________\n')


"""
delattr() - deletes an attribute from the object
If you are accessing the attribute after deleting, it raises AttributeError

The method takes two parameters: Object, Name
"""


class Person:
    def __init__(self, name):
        self.name = name


person = Person('Peter')
print(person.name)                 # Peter
print(delattr(person, 'name'))     # None
print(person.name)                 # AttributeError


print('\n_________ __delattr__() _________\n')


"""
Called when an attribute deletion is attempted.

The method takes 1 parameter: The 'Name" of the attribute
It should only be implemented if del obj.name is meaningful for the object
"""


class Phone:
    def __delattr__(self, attr):
        del self.__dict__[attr]
        print(f"'{str(attr)}' was deleted")


phone = Phone()
phone.color = 'black'
del phone.color  # 'color' was deleted
