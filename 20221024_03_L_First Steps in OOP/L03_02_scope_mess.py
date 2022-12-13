# 20221024 - Python OOP - First Steps in OOP
# 02 - Scope Mess - judge url: https://judge.softuni.org/Contests/Practice/Index/1934#1


# --------------------- version 1 --------------------- judge 100%


x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()


print(x)
outer()
print(x)
