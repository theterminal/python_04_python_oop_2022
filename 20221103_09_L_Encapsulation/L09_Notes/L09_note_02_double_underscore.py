# 20221103 - Python - Python OOP - Encapsulation
# note 02 - Double Underscore (PRIVATE method / variable)


"""
When naming an attribute with two leading underscores, it invokes name mangling.
In Python, mangling is used for attributes that one class does not want subclasses to use.
Python does not restrict access to such attributes.
It is still possible to access or modify a variable that is considered "private" from outside the class.

Formula for outside access: _ClassName__MethodName
Formula for outside access: _ClassName__AttributeName
"""


class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age

    def info(self):
        print(f"I am {self.name}, {self.__age} years old.")


person = Person('Peter', 25)


# accessing data using the class method
person.info()	                                    # I am Peter, 25 years old.

# accessing data directly from outside
print(person.name)	                                # Peter
print(person.__age)                                 # AttributeError: 'Person' object has no attribute '__age'
