# 20221117 - Python - Python OOP - Iterators and Generators
# 02 - Reverse Iter - judge url: https://judge.softuni.org/Contests/Practice/Index/1944#1


class reverse_iter:
    def __init__(self, iterable):
        self.iterable = list(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.iterable:
            raise StopIteration
        return self.iterable.pop()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
