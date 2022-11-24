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


print('\n________________ example 3 _________________\n')


def first_n(number):
    num = 0
    while num < number:
        yield num
        num += 1


sum_of_numbers = 0
for n in first_n(5):
    sum_of_numbers += n

print(sum_of_numbers)


print('\n________________ example 4 _________________\n')


def first_n(number):
    num = 0
    while num < number:
        yield num
        num += 1


a = first_n(5)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
# print(next(a))                # Traceback (most recent call last):
#                               #   File "/Users/borasam/PycharmProjects/python_04_python_oop_2022/20221117_17_L_Iterators_and_Generators/L17_Notes/L17_note_03_generators.py", line 77, in <module>
#                               #     print(next(a))
#                               # StopIteration


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
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


print(my_gen())                         # <generator object my_gen at 0x10269cc10>

for n in my_gen():
    print(n)                            # This is printed first
#                                       # 1
#                                       # This is printed second
#                                       # 2
#                                       # This is printed at last
#                                       # 3
