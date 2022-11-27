# 20221121 - Python - Python OOP - Decorators
# 01 - Number Increment - judge url: https://judge.softuni.org/Contests/Practice/Index/1946#0


def number_increment(numbers):
    def increase():
        return [x + 1 for x in numbers]

    return increase()


print(number_increment([1, 2, 3]))
