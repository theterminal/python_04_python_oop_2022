# 20221121 - Python - Python OOP - Decorators
# Note 04 - Creating Decorators using *args


from functools import wraps


"""
Sometimes, we might need to define a decorator that accepts arguments.
We achieve this by passing the arguments to the wrapper function.
The arguments will then be passed to the function that is being decorated at call time.
"""


print('\n____________________ example 1 _____ using 1 argument and not using *args _____________________\n')


def vowel_filter(fun):
    vowels = 'aoiuye'

    @wraps(fun)
    def wrapper(word):
        result = fun(word)
        return [x for x in result if x.lower() in vowels]

    return wrapper


@vowel_filter
def get_letters(word):
    return list(word)


print(get_letters('Ilina'))             # It'll be a problem if you give 2 positional arguments instead of 1...


print('\n___________________ example 2 _____ using 0, 1 and 3 arguments and using *args ___________________\n')


def vowel_filter(fun):
    vowels = 'aoiuye'

    @wraps(fun)
    def wrapper(*args):
        result = fun(*args)
        return [x for x in result if x.lower() in vowels]

    return wrapper


@vowel_filter
def get_letters_1(name):
    return list(name)


@vowel_filter
def get_letters_2(name_1, name_2, name_3):
    return list(name_1) + list(name_2) + list(name_3)


@vowel_filter
def get_letters_3():
    return f'say whatever...'


print(get_letters_1('Ilina'))                                   # ['I', 'i', 'a']                   - Using 1 argument
print(get_letters_2('Ilina', 'Kim', 'Sunny'))                   # ['I', 'i', 'a', 'i', 'u', 'y']    - Using 3 arguments
print(get_letters_3())                                          # ['a', 'y', 'a', 'e', 'e']         - Using 0 arguments
