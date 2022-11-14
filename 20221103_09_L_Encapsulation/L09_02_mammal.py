# 20221103 - Python - Python OOP - Encapsulation
# 02 - Mammal - judge url: https://judge.softuni.org/Contests/Practice/Index/1938#1


class Mammal:
    __kingdom = 'animals'

    def __init__(self, name: str, type: str, sound: str):
        self. name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        return f'{self.name} makes {self.sound}'

    def get_kingdom(self):
        return Mammal.__kingdom

    def info(self):
        return f'{self.name} is of type {self.type}'


mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())
