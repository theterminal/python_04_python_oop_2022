# Abstract Class Example 1


from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        raise NotImplementedError("Subclass must implement")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Bark!")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Meow!")


cat = Cat("Willy")
cat.sound()                                         # Meow!

dog = Dog("Willy")
dog.sound()                                         # Bark!

animal = Animal("Willy")                            # TypeError: Can't instantiate abstract class Animal with abstract method sound
animal.sound()


# ___________ result is as follows ____________


# Meow!
# Bark!
# Traceback (most recent call last):
#   File "/Users/borasam/PycharmProjects/python_04_python_oop_2022/20221110_13_L_Polymorphism_and_Abstraction/L13_Notes/L13_note_08_abstract_class_example_1.py", line 38, in <module>
#     animal = Animal("Willy")                            # TypeError: Can't instantiate abstract class Animal with abstract method sound
# TypeError: Can't instantiate abstract class Animal with abstract method sound
