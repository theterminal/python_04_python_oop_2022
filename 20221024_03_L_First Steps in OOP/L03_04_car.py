# 20221024 - Python OOP - First Steps in OOP
# 04 - Car - judge url: https://judge.softuni.org/Contests/Practice/Index/1934#3


# --------------------- version 1 --------------------- judge 100%


class Car:
    def __init__(self, name: str, model: str, engine: str):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f'This is {self.name} {self.model} with engine {self.engine}'


car = Car("Kia", "Rio", "1.3L B3 I4")
print(car.get_info())
