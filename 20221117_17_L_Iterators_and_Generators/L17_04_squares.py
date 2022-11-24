# 20221117 - Python - Python OOP - Iterators and Generators
# 04 - Squares - judge url: https://judge.softuni.org/Contests/Practice/Index/1944#3


# __________ version 1 ______ using generator ____________


def squares(n):
    num = 1
    while num <= n:
        yield num ** 2
        num += 1


print(list(squares(5)))


# __________ version 2 ______ using iterator _____________


class Squares:
    def __init__(self, end: int):
        self.start = 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        self.start += 1
        return (self.start - 1) ** 2


print(list(Squares(5)))


# Note: Using iterator you could make your class to be AND iterator among other uses.
