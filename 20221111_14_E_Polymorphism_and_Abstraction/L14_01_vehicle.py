# 20221111 - Python - Python OOP - Polymorphism and Abstraction
# 01 - Vehicle - judge url: https://judge.softuni.org/Contests/Compete/Index/1943#0


from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float):
        pass

    @abstractmethod
    def refuel(self, fuel: float):
        pass


class Car(Vehicle):
    ADDITIONAL_FUEL_PER_KM = 0.9

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance: float):
        consumption = (self.fuel_consumption + Car.ADDITIONAL_FUEL_PER_KM) * distance
        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    ADDITIONAL_FUEL_PER_KM = 1.6

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance: float):
        consumption = (self.fuel_consumption + Truck.ADDITIONAL_FUEL_PER_KM) * distance
        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel * 0.95


print('\n______________ Test Code 1 _________________\n')
car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)


print('\n______________ Test Code 2 _________________\n')
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
