# 20221103 - Python - Python OOP - Encapsulation
# 01 - Person - judge url: https://judge.softuni.org/Contests/Practice/Index/1938#0


class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


person = Person("George", 32)
print(person.get_name())
print(person.get_age())
