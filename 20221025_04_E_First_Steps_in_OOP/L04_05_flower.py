# 20221025 - Python OOP - First Steps in OOP
# 05 - Flower - judge: https://judge.softuni.org/Contests/Compete/Index/1935#4


# --------------------- version 1 ------------------------ judge: 100%


class Flower:
    def __init__(self, name: str, water_requirements: int):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity):
        if quantity >= self.water_requirements:
            self.is_happy = True
        else:
            self.is_happy = False

    def status(self):
        return f"{self.name} is{'' if self.is_happy else ' not'} happy"

        # if self.is_happy:
        #     return f'{self.name} is happy'
        # else:
        #     return f'{self.name} is not happy'


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())
