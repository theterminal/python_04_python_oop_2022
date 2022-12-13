# 20221024 - Python OOP - First Steps in OOP
# Note 07 - Creating a class with one method inside


class Animal:
    def __init__(self, name: str):                  # initializing method
        self.name = name

    def is_asleep(self):                            # method (defines an action for the object)
        return f'{self.name} is sleeping!'


animal_1 = Animal('The Big Bear')
print(animal_1.is_asleep())                         # The Big Bear is sleeping!

animal_2 = Animal('The Pink Panther')
print(animal_2.is_asleep())                         # The Pink Panther is sleeping!
