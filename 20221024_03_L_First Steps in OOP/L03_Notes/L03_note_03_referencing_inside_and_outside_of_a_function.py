# 20221024 - Python OOP - First Steps in OOP
# Note 03 - Referencing data type inside and outside of functions


def f():
    elements.append(4)
    print(elements)


elements = [1, 2, 3]
print(elements)
f()
print(elements)

'''

As it is visible from the result, the REFERENCING type of data CAN be changed from inside of a function without
being specifically given as an argument to the function.

Same is NOT possible with a NON-REFERENCING data type, number for example.

In other words the reference to the data cannot be changed from inside a function without data 
being imported as an argument first!

The appending of the list in the example is possible due to the same reason.
We are not assigning new data carrier but we are adding to the already existing data, just referencing it.   

'''
