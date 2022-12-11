# 20221118 - Python - Python OOP - Iterators and Generators
# Note 02 - Iterator


class CountdownIterator:
    def __init__(self, count: int):
        self.count = count

    def __iter__(self):
        return iter('abc')                         # could use: iter(['abc', 'def']), iter({'abc', 'def'})

    def __next__(self):
        if self.count < 0:
            raise StopIteration
        self.count -= 1
        return self.count + 1


iterator = CountdownIterator(10)
for item in iterator:
    print(item, end=" ")                           # a b c
