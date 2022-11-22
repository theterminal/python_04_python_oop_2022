# 20221117 - Python - Python OOP - Iterators and Generators
# 01 - Custom Range - judge url: https://judge.softuni.org/Contests/Practice/Index/1944#0


class custom_range:                                 # The name of the class must be 'custom_range' for the judge test
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.counter = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > self.end:
            raise StopIteration
        result = self.counter
        self.counter += 1
        return result


for element in custom_range(1, 10):
    print(element)
