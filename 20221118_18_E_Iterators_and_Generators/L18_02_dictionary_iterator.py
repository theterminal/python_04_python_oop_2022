# 20221118 - Python - Python OOP - Iterators and Generators
# 02 - Dictionary Iterator - judge url: https://judge.softuni.org/Contests/Compete/Index/1945#1


class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.items = list(dictionary.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        result = self.items[self.index]
        self.index += 1
        return result


input_data = dictionary_iter({1: "1", 2: "2"})
for x in input_data:
    print(x)
