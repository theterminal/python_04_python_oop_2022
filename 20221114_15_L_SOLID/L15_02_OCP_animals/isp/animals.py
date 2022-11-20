from abc import ABC, abstractmethod


# ________________ end code _____________________


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        ...


class Cat(Animal):
    def make_sound(self):
        return 'meow'


class Dog(Animal):
    def make_sound(self):
        return 'bark'


class Chicken(Animal):
    def make_sound(self):
        return 'clutch'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Chicken()]
animal_sound(animals)


# ________________ start code ___________________


# class Animal:
#     def __init__(self, species):
#         self.species = species
#
#     def get_species(self):
#         return self.species
#
#
# def animal_sound(animals: list):
#     for animal in animals:
#         if animal.species == 'cat':
#             print('meow')
#         elif animal.species == 'dog':
#             print('woof-woof')
#
#
# animals = [Animal('cat'), Animal('dog')]
# animal_sound(animals)
#
# # animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
