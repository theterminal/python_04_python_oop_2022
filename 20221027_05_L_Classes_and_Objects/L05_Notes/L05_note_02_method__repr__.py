# 20221027 - Python OOP - Classes and Objects
# Note 2 - Method __repr__


print('\n---------- print with __repr__ method (easier when in debug mode) ------------------\n')


class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def change_year(self, new_year):
        self.year = new_year

    def __repr__(self):                                     # When in debug, it shows this string type and not object
        return f'{self.model} made {self.year}'


nissan = Car('GT-R', 2012)
toyota = Car('Supra', 1999)

cars = [nissan, toyota]

for car in cars:
    print(car)                                              # any of the 4 lines work
    print(str(car))
    print(car.__str__())
    print(car.__repr__())
