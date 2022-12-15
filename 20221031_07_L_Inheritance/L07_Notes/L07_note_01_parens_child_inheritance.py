# 20221031 - Python OOP - Inheritance
# Note 01 - Parents, child inheritance


class A:
    def f_a(self):
        return f'f from A'


class B:
    def f_b(self):
        return f'f from B'


class C(A, B):
    pass


c = C()
print(c.f_a())                      # f from A
print(c.f_b())                      # f from B
