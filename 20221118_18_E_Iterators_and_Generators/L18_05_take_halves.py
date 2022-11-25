# 20221118 - Python - Python OOP - Iterators and Generators
# 05 - Take Halves - judge url: https://judge.softuni.org/Contests/Compete/Index/1945#4


def solution():
    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        # __________ block 1 _____________ use block 1 or block 2 ____________
        # return [next(seq) for _ in range(n)]

        # __________ block 2 _____________ use block 1 or block 2 ____________
        result = []
        for x in range(n):
            result.append(next(seq))
        return result

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
