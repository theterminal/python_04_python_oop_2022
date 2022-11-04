# 20221027 - Python OOP - Classes and Objects
# 03 - Circle - judge: https://judge.softuni.org/Contests/Practice/Index/1936#2


# --------------------- version 1 ------------------------ judge: 100%


class Circle:
    pi = 3.14

    def __init__(self, radius: float):
        self.radius = radius

    def set_radius(self, new_radius: float):
        self.radius = new_radius

    def get_area(self):
        return (self.radius ** 2) * Circle.pi

    def get_circumference(self):
        return 2 * Circle.pi * self.radius                      # could use 'self.pi' instead 'Circle.pi'


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
