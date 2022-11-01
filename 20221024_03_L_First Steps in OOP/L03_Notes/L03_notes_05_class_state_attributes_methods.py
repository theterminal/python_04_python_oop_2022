# 20221024 - Python OOP - First Steps in OOP
# Notes 03


print('\n------------------- creating a class with one method --------------------\n')


class Animal:
    def __init__(self, name: str):                  # initializing method
        self.name = name

    def is_asleep(self):                            # method (defines an action for the object)
        return f'{self.name} is sleeping!'


animal_1 = Animal('The Big Bear')
print(animal_1.is_asleep())

animal_2 = Animal('The Pink Panther')
print(animal_2.is_asleep())


"""


The Big Bear is sleeping!
The Pink Panther is sleeping!


"""


print('\n--- creating a class with one method where the attribute is a function of the class ---\n')


class Person:
    def __init__(self, first_name, last_name):
        self.name = self.get_full_name(first_name, last_name)

    def get_full_name(self, first_name, last_name):
        return f'{first_name} {last_name}'


test = Person('Alex', 'Jones')
print(test.name)
