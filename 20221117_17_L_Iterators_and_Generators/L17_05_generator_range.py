# 20221117 - Python - Python OOP - Iterators and Generators
# 05 - Generator Range - judge url: https://judge.softuni.org/Contests/Practice/Index/1944#4


print('\n_____ version 1 _____ using "while loop" _____\n')


def genrange(start: int, end: int):
    num = start
    while num <= end:
        yield num
        num += 1


print(list(genrange(1, 10)))


print('\n_____ version 2 _____ using "for loop" _____\n')


def genrange(start: int, end: int):
    for num in range(start, end + 1):
        yield num


print(list(genrange(1, 10)))
