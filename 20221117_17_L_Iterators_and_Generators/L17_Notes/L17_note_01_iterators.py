# 20221117 - Python - Python OOP - Iterators and Generators
# Note 01 - Iterators


"""
Iterator is simply an object that can be iterated upon.
An object which will return data, one element at a time.

Iterator object must implement two methods, __iter__() and __next__() (iterator protocol).
NOT only those methods but at least those 2.

An object is called iterable if we can get an iterator from it.
Such are: list, tuple, string, etc...
"""

# EXAMPLE iterator:
# The iter() function (which calls the __iter__() method) returns an iterator from an iterable.


my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)
print(next(my_iter))       # 4
print(next(my_iter))       # 7
print(my_iter.__next__())  # 0
print(my_iter.__next__())  # 3
next(my_iter)              # Error
