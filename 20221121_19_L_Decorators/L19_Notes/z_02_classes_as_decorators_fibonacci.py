# 20221121 - Python - Python OOP - Decorators
# Note 10 - Classes as Decorators


# ___________________ version 1 ______________________


# The correct way of doing it

class Fibonacci:
    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[0] = 0
            elif n == 1:
                self.cache[1] = 1
            else:
                self.cache[n] = self(n-1) + self(n-2)
        return self.cache[n]


f = Fibonacci()

for i in range(499):
    print(f'Fibonacci of {i} is: {f(i):_}')

print('\nFull cache is:' + '\n' + f'{f.cache}')


# ___________________ version 2 ______________________


# not practical due to the recursive nature of the calculation.


# class Fibonacci:
#     def __call__(self, n):
#         if n < 2:
#             return 1
#         return self(n - 1) + self(n - 2)
#
#
# f = Fibonacci()
# print(f'{f(40):,}')
