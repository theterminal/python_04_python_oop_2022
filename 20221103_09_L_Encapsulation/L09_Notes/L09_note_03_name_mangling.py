# 20221103 - Python - Python OOP - Encapsulation
# Note 03 - Name Mangling


"""

Used to show that the variable should not be accessed outside the class

Formula for outside access: _ClassName__MethodName
Formula for outside access: _ClassName__AttributeName

"""


class Car:
    def __init__(self):
        self.__max_speed = 200

    def drive(self):
        print(f'driving max speed {self.__max_speed}')


red_car = Car()
red_car.drive()                 # driving max speed 200
red_car.__max_speed = 10        # won't change because it is name mangled
red_car.drive()                 # driving max speed 200
