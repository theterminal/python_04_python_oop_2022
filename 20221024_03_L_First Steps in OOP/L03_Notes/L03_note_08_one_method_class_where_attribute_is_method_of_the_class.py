# 20221024 - Python OOP - First Steps in OOP
# Note 08 - Creating a class with one method where the attribute is a function of the class


class Person:
    def __init__(self, first_name, last_name):
        self.name = self.get_full_name(first_name, last_name)

    def get_full_name(self, first_name, last_name):
        return f'{first_name} {last_name}'


test = Person('Alex', 'Jones')
print(test.name)
