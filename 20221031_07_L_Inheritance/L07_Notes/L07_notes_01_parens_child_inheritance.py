# 20221031 - Python OOP - Inheritance


class A:
    def f_a(self):
        return f'f from A'


class B:
    def f_b(self):
        return f'f from B'


class C(A, B):
    pass


c = C()
print(c.f_a())
print(c.f_b())
