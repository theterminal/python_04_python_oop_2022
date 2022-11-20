# 20221114 - Python - Python OOP - SOLID
# Note 01 - SRP (Single Responsibility Principle)


"""
Each class is responsible for only one thing and should have only one reason to change.
A class that has many responsibilities is coupling these responsibilities together,
which leads to complexity and fragility.

"""


# _________________ SRP Violations __________________


"""
SRP states that classes should have one responsibility. Here we have two:
    *) student properties management
    *) student database management
"""


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_info(self):
#         return f'{self.name} is {self.age} years old.'
#
#     def register(self, student):
#         return ...


# __________________ Correct way to do it ______________


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'{self.name} is {self.age} years old.'


class Registration:
    def __init__(self):
        self.students = []

    def register(self, student: Student):
        for s in self.students:
            if s.name == student.name:
                raise Exception(f'Student {student.name} is already registered!')
        self.students.append(student)

    def details(self):
        result = ''
        for student in self.students:
            result += student.get_info() + '\n'
        return result


r = Registration()

r.register(Student('Peter', 18))
r.register(Student('Ivan', 19))
r.register(Student('George', 49))
# r.register(Student('Peter', 18))          # It'll return an Exception because this student is already registered.

print(r.details())
