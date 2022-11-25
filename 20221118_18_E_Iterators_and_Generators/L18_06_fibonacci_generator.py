# 20221118 - Python - Python OOP - Iterators and Generators
# 06 - Fibonacci Generator - judge url: https://judge.softuni.org/Contests/Compete/Index/1945#5


# _________________ version 2 _______________


def fibonacci():
    num_1, num_2 = 0, 1
    while True:
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2


# Test Code 1
generator = fibonacci()
for i in range(50):
    print(f"{next(generator):,}")

# Test Code 2
generator = fibonacci()
for i in range(1):
    print(next(generator))


# _________________ version 1 _______________


def fibonacci():
    num_1 = 0
    num_3 = num_1
    yield num_3

    num_2 = 1
    num_3 = num_2
    yield num_3

    num_3 = num_1 + num_2
    while True:
        yield num_3
        num_1 = num_2
        num_2 = num_3
        num_3 = num_1 + num_2


# Test Code 1
generator = fibonacci()
for i in range(5):
    print(next(generator))

# Test Code 2
generator = fibonacci()
for i in range(1):
    print(next(generator))
