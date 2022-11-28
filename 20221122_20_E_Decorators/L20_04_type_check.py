# 20221122 - Python - Python OOP - Decorators
# 04 - Type Check - judge url: https://judge.softuni.org/Contests/Compete/Index/1947#3


def type_check(expected_type):                              # 'int' (line 15) goes as 'expected_type' in the 'type_check' function
    def decorator(func):                                    # 'func' in this case is 'times2' referent of the function 'times2()'
        def wrapper(arg):                                   # wrapper function is executed when we call it with arguments (line 20 in this case)
            if not isinstance(arg, expected_type):          # in this case 'int' (line 15) must be same type as 'num' (line 16)
                return f'Bad Type'                          # return if 'arg' is not same type as 'expected_type'
            return func(arg)                                # 'func(arg)' is executed if types match
        return wrapper
    return decorator


# _______________ Test Code 1 ____________________


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))                                            # 'wrapper' function is executed when called
print(times2('Not A Number'))


# _______________ Test Code 2 ____________________


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
