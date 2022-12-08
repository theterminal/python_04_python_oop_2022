# 20221024 - Python OOP - First Steps in OOP
# Note 02 - Function Shadow


def sum(elements):
    result = 1
    for el in elements:
        result *= el
    return result


print(sum([1, 2, 3, 4]))


'''

As is visible from the example the name of our function 'sum' overrides the built-in function sum.
Not a good idea to do it!

'''

