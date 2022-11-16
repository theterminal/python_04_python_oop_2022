# 20221107 - Python - Python OOP
# Note 02 - Class Methods


"""
It is bound to the class and not the object of the class.
It can modify a class state that would apply across all the instances of the class.
To turn a method into a class method, we add a line with @classmethod in front of the method header.

We generally use class method to create factory methods.

Benefits:
--------
Simply provide a shortcut for creating new instance objects.
Ensures correct instance creation of the derived class.
You could easily follow the Don't Repeat Yourself (DRY) principle using class methods.
"""


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def pepperoni(cls):
        return cls(['tomato sauce', 'parmesan', 'pepperoni'])

    @classmethod
    def quattro_formaggi(cls):
        return cls(['mozzarella', 'gorgonzola', 'fontina', 'parmigiana'])


pizza_1 = Pizza.pepperoni()
pizza_2 = Pizza.quattro_formaggi()

print(pizza_1)                                  # newly created instance 'pizza_1'
print(pizza_2)                                  # newly created instance 'pizza_2'
