# 20221103 - Python - Python OOP - Encapsulation
# note 09 - Function getattr() and method __getattr()__


print('\n________________ function getattr() ___________________\n')


"""
getattr()
Used to access the attribute of an object.
Returns the value of the named attribute .

The method takes multiple parameters: 'Object', 'Name', 'Default' (optional)
"""


class Person:
    def __init__(self, name):
        self.name = name


person = Person('Peter')
print(getattr(person, 'name'))                  # True
# print(getattr(person, 'age'))                 # AttributeError
print(getattr(person, 'age', 'None'))           # None


print('\n________________ method __getattr__() _____ ex. 1 ______\n')


"""
Called when an attribute lookup has not found the attribute in the usual places.
The method takes 1 parameter – the 'Name' of the attribute

When accessing 'phone.color', Python calls "phone.__getattr__('color')"
"""


# class Phone:
#     def __getattr__(self, attr):
#         return None
#
#
# phone = Phone()
# print(phone.color)                              # None
# print(getattr(phone, 'size'))                   # None


print('\n------------------------ ex. 2 ------------------------\n')


# class Phone:
#     def __getattr__(self, attr):
#         return attr
#
#
# phone = Phone()
# print(phone.color)                              # color
# print(getattr(phone, 'size'))                   # size


print('\n------------------------ ex. 3 ------------------------\n')


# class Phone:
#     def __init__(self, color: str, size: int):
#         self.color = color
#         self.size = size
#
#     def __getattr__(self, attr):
#         return None
#
#
# phone = Phone('blue', 12)
# print(phone.color)                              # None only if attr is missing
# print(getattr(phone, 'size'))                   # None only if attr is missing


print('\n------------------------------------------------------\n')
