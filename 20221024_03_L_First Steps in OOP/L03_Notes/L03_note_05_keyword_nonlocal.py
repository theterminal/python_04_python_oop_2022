# 20221024 - Python OOP - First Steps in OOP
# Note 05 - Keyword "nonlocal"


def f_1():
    text = 'Sofia'
    print(text, f'- From f_1()')

    def f_2():
        print(text, '- From inside f_2(), as first line after the def statement.')

        def f_3():
            nonlocal text
            text = 'Moscow'
            print(text, '- From inside of f_3()')

        f_3()
        print(text, '- From inside of f_2(), after definition of f_3() and statement nonlocal inside f_3(), that actually changed the variable')

    f_2()


text = 'Washington DC'
print(text, '- Variable "text" initiated from outside of the functions')

f_1()
print(text, '- Same variable "text" initiated from outside of the functions but printed after calling of the function.')


"""


The variable 'text' declared outside the functions is different from the variable 'text' from the inside the functions.
The variable 'text' declared inside f_1() is the same variable inside f_2() and f_3(). 


"""
