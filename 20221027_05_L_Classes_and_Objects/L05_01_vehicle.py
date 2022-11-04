# 20221027 - Python OOP - Classes and Objects
# 01 - Vehicle - judge: https://judge.softuni.org/Contests/Practice/Index/1936#0


# --------------------- version 1 ------------------------ judge: 100%


class Vehicle:
    def __init__(self, mileage: float, max_speed=150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []


car = Vehicle(20)

print(car.max_speed)
print(car.mileage)
print(car.gadgets)

car.gadgets.append('Hudly Wireless')
print(car.gadgets)
