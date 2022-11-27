# 20221121 - Python - Python OOP - Decorators
# 02 - Vowel Filter - judge url: https://judge.softuni.org/Contests/Practice/Index/1946#1


# _____________ version 3 _______________


def vowel_filter(fun):
    vowels = 'aoiuye'

    def wrapper():
        return [x for x in fun() if x.lower() in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())


# _____________ version 2 _______________


def vowel_filter(function):
    vowels = 'aoiuye'

    def wrapper():
        result = function()
        return [x for x in result if x.lower() in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())


# _____________ version 1 _______________


def vowel_filter(function):
    vowels = ['a', 'o', 'i', 'u', 'y', 'e']
    result = []

    def wrapper():
        for el in function():
            if el.lower() in vowels:
                result.append(el)
        return result

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
