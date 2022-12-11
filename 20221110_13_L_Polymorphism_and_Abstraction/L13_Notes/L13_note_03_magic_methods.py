# 20221110 - Python - Python OOP
# Note 3 - Magic Methods

"""

__add__(self, other)                        +
__sub__(self, other)                        _
__mul__(self, other)                        *
__floordiv__(self, other)                   //
__truediv__(self, other)                    /
__pow__(self, other[, modulo])              **

"""


print('\n------------------ Example overloading __add__() --------------------\n')


"""

If we have a class Purchase and we want to sum all expenses using the + operator, we can override the __add__ method

"""


class Purchase:
    def __init__(self, product_name, cost):
        self.product_name = product_name
        self.cost = cost

    def __add__(self, other):
        name = f'{self.product_name}, {other.product_name}'
        cost = self.cost + other.cost
        return Purchase(name, cost)                             # returns a new instance of the class 'Purchase'

    def __repr__(self):
        return f'{self.product_name}; {self.cost}'


purchase_1 = Purchase('sofa', 650)
purchase_2 = Purchase('table', 150)

print(purchase_1 + purchase_2)                             # sofa, table; 800
