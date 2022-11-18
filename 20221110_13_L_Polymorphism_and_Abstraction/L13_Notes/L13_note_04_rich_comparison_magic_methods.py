# Rich Comparison Magic Methods


"""

__lt__(self, other)         <
__le__(self, other)         <=
__eq__(self, other)         ==
__ne__(self, other)         !=
__gt__(self, other)         >
__ge__(self, other)         >=

"""


# Example: Overloading __gt__()


class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary


person_one = Person('John', 20)
person_two = Person('Natasha', 36)
print(person_one > person_two)                                      # False
