# 20221118 - Python - Python OOP - Iterators and Generators
# 07 - Reader - judge url: https://judge.softuni.org/Contests/Compete/Index/1945#6


def read_next(*args):
    for el in args:
        for sub_el in el:
            yield sub_el


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)