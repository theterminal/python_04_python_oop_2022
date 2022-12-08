# 20221027 - Python OOP - Classes and Objects
# Note 1 - Method __str__


print('\n---------- print without __str__ method ------------------\n')


class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def change_year(self, new_year):
        self.year = new_year


nissan = Car('GT-R', 2012)
toyota = Car('Supra', 1999)

cars = [nissan, toyota]

for car in cars:
    print(car)                                  # prints out the object and the address of residence


print('\n---------- print with __str__ method ------------------\n')


class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def change_year(self, new_year):
        self.year = new_year

    def __str__(self):
        return f'{self.model} made {self.year}'


nissan = Car('GT-R', 2012)
toyota = Car('Supra', 1999)

cars = [nissan, toyota]

for car in cars:
    print(car)                                              # any of the 3 lines work
    print(str(car))
    print(car.__str__())
