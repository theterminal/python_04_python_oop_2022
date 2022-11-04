# 20221027 - Python OOP - Classes and Objects
# 02 - Point - judge: https://judge.softuni.org/Contests/Practice/Index/1936#1


# --------------------- version 1 ------------------------ judge: 100%


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def set_x(self, new_x: float):
        self.x = new_x

    def set_y(self, new_y: float):
        self.y = new_y

    def __str__(self):
        return f'The point has coordinates ({self.x},{self.y})'


p = Point(2, 4)
print(p)
p.set_x(3)
p.set_y(5)
print(p)
