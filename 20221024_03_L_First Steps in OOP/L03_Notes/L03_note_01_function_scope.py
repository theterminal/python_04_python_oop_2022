# 20221024 - Python OOP - First Steps in OOP
# Notes 01 - Function Scope

from math import pi


def f():
    pi = 4.23
    print(pi)


print(pi)                                           # 3.141592653589793
f()                                                 # 4.23
print(pi)                                           # 3.141592653589793
f()                                                 # 4.23


"""

pi inside f() and pi outside f() are two different variables.

"""
