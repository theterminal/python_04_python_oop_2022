# 20221024 - Python OOP - First Steps in OOP
# Notes 01


print('\n__________ function scope ____________\n')

from math import pi


def f():
    pi = 4.23
    print(pi)


print(pi)
f()
print(pi)
f()

'''


pi inside f() and pi outside f() are two different variables.


'''

print('\n__________ function shadow ____________\n')


def sum(elements):
    result = 1
    for el in elements:
        result *= el
    return result


print(sum([1, 2, 3, 4]))

'''


As is visible from the example the name of our function 'sum' overrides the built-in function sum.
Not a good idea to do it!


'''

print('\n__________ referencing data type inside and outside of functions ____________\n')


elements = [1, 2, 3]


def f():
    elements.append(4)
    print(elements)


print(elements)
f()


'''


As it is visible from the result, the referencing type of data could be changed from inside of a function without
being specifically given as an argument to the function. Same is not possible with a non-referencing data type,
number for example. In other words the reference to the data cannot be changed from inside a function without data 
being imported as an argument first. The appending of the list in the example is possible due to the same reason.
We are not assigning new data carrier but we are adding to the already existing data, just referencing it.   


'''
