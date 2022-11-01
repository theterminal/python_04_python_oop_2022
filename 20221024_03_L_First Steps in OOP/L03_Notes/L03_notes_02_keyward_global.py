# 20221024 - Python OOP - First Steps in OOP
# Notes 02


print('\n__________ keyword "global" ____________\n')


def f():
    global num
    num += 100
    print(num)


def f_2():
    global num
    num += 1000


num = 42

print(num)
f()
print(num)
f_2()
print(num)


"""


When 'global' keyword is used, the variable 'num' initialized out of the function's scope is accessible inside the
function/s.


"""
