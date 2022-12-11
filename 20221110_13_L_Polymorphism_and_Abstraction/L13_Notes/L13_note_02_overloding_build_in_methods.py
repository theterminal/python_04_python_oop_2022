# 20221110 - Python - Python OOP
# Note 2 - Overloading built-in methods


"""

Overloading is when one and the same function returns different result (functionality) based on the input data!
Overloading is adding more functionality.

Example below. Overloading function 'len'. The function 'len' continues to exist but on 'MyClass' it returns my
functionality. It is close to polymorphism, but it is overloading in its core.

"""


class MyClass:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __len__(self):                                      # overloading
        return self.size


my_class = MyClass("Class Name", 3)
print(len(my_class))                                        # 3


"""

Another example of overloading:

integer = 1 + 1
string = "Hello, " + "SoftUni"
list = ["1", "2"] + ["3", "4"]

With '+' you can add 2 numbers or concatenate strings or combine 2 lists into one list.

"""
