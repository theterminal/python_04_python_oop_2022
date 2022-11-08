from project_07_02.animal import Animal
from project_07_02.dog import Dog


animal_1 = Animal()
print(animal_1.eat())

try:
    print(animal_1.bark())                  # object has no attribute 'bark'
except AttributeError:
    print('object has no attribute "bark"')

dog_1 = Dog()
print(dog_1.eat())
print(dog_1.bark())
