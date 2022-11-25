# 20221118 - Python - Python OOP - Iterators and Generators
# 04 - Sequence Repeat - judge url: https://judge.softuni.org/Contests/Compete/Index/1945#3


# _________________ version 1 ____________________


class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = list(sequence)
        self.number = number
        self.counter = 0
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.sequence) - 1:
            self.index = -1
        self.index += 1

        if self.counter == self.number:
            raise StopIteration
        self.counter += 1

        return self.sequence[self.index]


# Test Code 1
result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

# Test Code 2
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')


# _________________ version 2 ____________________


class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = list(sequence)
        self.number = number
        self.counter = 0
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.number - 1:
            raise StopIteration
        self.index += 1

        return self.sequence[self.index % len(self.sequence)]


# Test Code 1
result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

# Test Code 2
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
