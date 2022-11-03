# 20221025 - Python OOP - First Steps in OOP
# 02 - Hero - judge: https://judge.softuni.org/Contests/Compete/Index/1935#1


# --------------------- version 1 ------------------------ judge: 100%


class Hero:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def defend(self, damage: int):
        self.health -= damage

        if self.health <= 0:
            self.health = 0
            return f'{self.name} was defeated'

    def heal(self, amount: int):
        self.health += amount
        return self.health


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
