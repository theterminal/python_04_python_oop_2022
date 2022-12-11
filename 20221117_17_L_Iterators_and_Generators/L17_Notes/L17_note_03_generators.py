# 20221117 - Python - Python OOP - Iterators and Generators
# Note 03 - Generators


"""

Generators are a simple way of creating iterators.
A generator is a function that returns an object (iterator).
This iterator can later be iterated over (one value at a time).
To see/print the elements loop can be used or another iterator type functionality.

"""


print('\n________________ example 1 _________________\n')


def first_n(n):
    num = 0
    while num < n:
        yield num
        num += 1


for n in first_n(5):
    print(n)


print('\n________________ example 2 _________________\n')


def first_n(n):
    num = 0
    while num < n:
        yield num
        num += 1


sum_first_n = sum(first_n(5))
print(sum_first_n)

list_first_n = list(first_n(5))
print(list_first_n)
