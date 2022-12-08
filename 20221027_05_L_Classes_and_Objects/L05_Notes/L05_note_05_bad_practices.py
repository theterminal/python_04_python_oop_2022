class Laptop:
    def __init__(self, model):
        self.model = model


my_laptop = Laptop("Swift")
print(my_laptop.model)

my_laptop.ram = 8

if my_laptop.ram:
    print('Yes', my_laptop.ram)

Laptop.brand = "Dell"
print(Laptop.brand)

del my_laptop.model

try:
    print(my_laptop.model)
except:
    print('No attribute "model"')

