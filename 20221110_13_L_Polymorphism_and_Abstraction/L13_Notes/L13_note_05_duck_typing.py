# Duck Typing


"""
Duck Typing is a type system used in dynamic languages.
"If it looks like a duck and quacks like a duck, it's a duck".
i.e., We don't care about objects' types, but whether they have the methods we need.

It looks like polymorphism but it is NOT because the 2 classes have nothing in common except the action of interest!
Basically in the example below, the 2 classes have NOTHING in common except the name of the method 'sound()'

"""


# Example of Duck Typing


class Cat:
    @staticmethod
    def sound():
        print("Meow!")


class Train:
    @ staticmethod
    def sound():
        print("Sound from wheels slipping!")


for any_type in Cat(), Train():
    any_type.sound()                                # Meow!
#                                                   # Sound from wheels slipping!
