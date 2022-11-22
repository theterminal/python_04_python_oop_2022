# 20221117 - Python - Python OOP - Iterators and Generators
# Note 02 - For loop as iterator


"""
The for loop can iterate automatically through the list
The for loop can iterate over any iterable
A for loop is implemented as:
"""

iter_obj = iter(iterable)
while True:
    try:
        element = next(iter_obj)            # get the next item
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break


"""
The for loop creates an iterator object (iter_obj) by calling iter() on the iterable
Inside the loop, it calls next() to get the next element and executes the body of the for loop with this value
After all the items exhaust, StopIteration is raised, which is internally caught, and the loop ends
"""
