# 20221118 - Python - Python OOP - Iterators and Generators
# 03 - Countdown Iterator - judge url: https://judge.softuni.org/Contests/Compete/Index/1945#2


class countdown_iterator:
    def __init__(self, count: int):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < 0:
            raise StopIteration
        self.count -= 1
        return self.count + 1


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
