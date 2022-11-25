# 20221118 - Python - Python OOP - Iterators and Generators
# 08 - Prime Numbers - judge url: https://judge.softuni.org/Contests/Compete/Index/1945#7


def get_primes(ints: list):
    for num in ints:
        if num <= 1:
            continue

        for number in range(2, num):
            if num % number == 0:
                break
        else:
            yield num


# Test Code 1
print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

# Test Code 2
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
