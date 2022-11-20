# 20221114 - Python - Python OOP - SOLID
# Note 02 - OCP (Open/Close Principle)


"""
Software entities like classes, modules, and functions should be open for extension but closed for modifications.

This can be achieved through:
    *) Abstraction
    *) Mix-ins
    *) Monkey-Patching
    *) Generic functions (using overloading)

"""


# ________________________ OCP Violation ___________________________


# Let's imagine that we want to make a 40% discount of the semester taxes to all students with grades above 5.


class StudentTaxes:
    def __init__(self, name, semester_tax, average_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.average_grade = average_grade

    def get_discount(self):
        if self.average_grade > 5:
            return self.semester_tax * 0.4


# Later we decide that we want to give a 20% discount to students with grades above 4


class StudentTaxes:
    def __init__(self, name, semester_tax, average_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.average_grade = average_grade

    def get_discount(self):
        if self.average_grade > 5:
            return self.semester_tax * 0.4
        elif self.average_grade > 4:
            return self.semester_tax * 0.2


# ___________________ OCP Approaches _____________________


class StudentTaxes:
    def __init__(self, name, semester_tax, average_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.average_grade = average_grade

    def get_discount(self):
        if self.average_grade > 5:
            return self.semester_tax * 0.4


class AdditionalDiscount(StudentTaxes):
    def get_discount(self):
        result = super().get_discount()
        if result:
            return result
        if 4 < self.average_grade <= 5:
            return self.semester_tax * 0.2
