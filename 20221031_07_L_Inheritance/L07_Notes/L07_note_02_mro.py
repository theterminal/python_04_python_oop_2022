# 20221031 - Python OOP - Inheritance
# Note 02 - MRO (Method Resolution Order)

class Parent:
    pass


class FirstChild(Parent):
    pass


class SecondChild(Parent):
    pass


class GrandChild(SecondChild, FirstChild):
    pass


print(GrandChild.mro())         # [<class '__main__.GrandChild'>, <class '__main__.SecondChild'>, <class '__main__.FirstChild'>, <class '__main__.Parent'>, <class 'object'>]
