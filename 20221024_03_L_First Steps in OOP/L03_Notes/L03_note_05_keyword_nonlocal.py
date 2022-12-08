# 20221024 - Python OOP - First Steps in OOP
# Note 05 - Keyword "nonlocal"


def f_1():
    text = 'Sofia'
    print(text, f'- From f_1()')

    def f_2():

        def f_3():
            nonlocal text
            text = 'Moscow'
            print(text, '- From inside of f_3()')

        f_3()
        print(text)

    f_2()


text = 'Washington DC'
print(text, '- Variable "text" initiated from outside of the functions')

f_1()
print(text, '- Same variable "text" initiated from outside of the functions but printed after calling of the function.')
