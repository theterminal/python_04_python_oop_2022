# 20221118 - Python - Python OOP - Iterators and Generators
# 09 - Possible Permutations - judge url: https://judge.softuni.org/Contests/Compete/Index/1945#8

from itertools import permutations


def possible_permutations(ints: list):
    for el in permutations(ints):
        yield list(el)


print('\n________ Test Code 1 __________\n')
[print(n) for n in possible_permutations([1, 2, 3])]

print('\n________ Test Code 2 __________\n')
[print(n) for n in possible_permutations([1])]
