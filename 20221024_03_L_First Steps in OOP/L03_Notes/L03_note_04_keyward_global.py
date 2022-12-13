# 20221024 - Python OOP - First Steps in OOP
# Note 04 - Keyword "global"


def f_1():
    global num
    num += 100


def f_2():
    global num
    num += 1000


num = 42
print(num)                              # 42

f_1()
print(num)                              # 142

f_2()
print(num)                              # 1142


"""

When 'global' keyword is used, the variable 'num' initialized out of the function's scope is accessible inside the
function/s.

"""
