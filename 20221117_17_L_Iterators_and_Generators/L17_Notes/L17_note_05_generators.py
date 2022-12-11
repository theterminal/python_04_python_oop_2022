# 20221117 - Python - Python OOP - Iterators and Generators
# Note 5 - Generators


"""

If a function contains at least one yield statement, it becomes a generator function.
Both yield and return will return a value from a function.
The difference between yield and return is that the return statement terminates a function entirely.
Yield, however pauses the function saving all its states, and later continues from there on successive calls.


Generator function contains one or more yield statements.
It returns an iterator but does not start execution immediately.
Methods like __iter__() and __next__() are implemented automatically.
Once the function yields, the function is paused.
When the function terminates, StopIteration is raised automatically on further calls.

"""


print('\n________________ example 5 _________________\n')


def my_gen():
    num = 10
    print("\nPrinted from the first 'print' statement")
    yield f"num = {num} - This is from the first yield"

    num += 10
    print("\nPrinted from the second 'print' statement")
    yield f"num = {num} - This is from the second yield"

    num += 10
    print("\nPrinted from the third 'print' statement")
    yield f"num = {num} - This is from the third yield"


# print(my_gen())                         # <generator object my_gen at 0x10269cc10>

for x in my_gen():
    print(x)


"""

The result from the generator above is:


Printed from the first 'print' statement
10 - This is from the first yield

Printed from the second 'print' statement
20 - This is from the second yield

Printed from the third 'print' statement
30 - This is from the third yield

"""
