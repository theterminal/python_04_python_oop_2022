# 20221117 - Python - Python OOP - Iterators and Generators
# Note 04 - Generators


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
# print(next(a))                Traceback (most recent call last):
#                                 File "/Users/borasam/PycharmProjects/python_04_python_oop_2022/20221117_17_L_Iterators_and_Generators/L17_Notes/L17_note_03_generators.py", line 77, in <module>
#                                   print(next(a))
#                               StopIteration
