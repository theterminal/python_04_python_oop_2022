# 20221114 - Python - Python OOP - SOLID
# Note 05 - ICP (Interface Segregation Principle)


"""
A client should not depend on methods it does not use.
A good way of ensuring this is by separation through multiple inheritance.
This is precisely the purpose of the mix-ins - to provide multiple clients with specific behaviours.
ISP is intended to keep a system decoupled and thus easier to refactor, change, and redeploy.

Python doesn't have interfaces
Languages that do have interfaces:
    *) Breaking them up too much ends up with interfaces implementing interfaces


______________ ISP Violations ____________________


    *) Class Shape draws rectangle and circle
    *) Class Circle or Rectangle implementing the Shape class must define the methods:
        - draw_rectangle() and
        - draw_circle()

"""


class Shape:
    def draw_rectangle(self):
        raise NotImplementedError

    def draw_circle(self):
        raise NotImplementedError


"""
    *) Class Rectangle implements the method draw_circle() it has no use of
    *) Class Circle implements method draw_rectangle()

"""


class Rectangle(Shape):
    def draw_rectangle(self):
        pass

    def draw_circle(self):
        pass


class Circle(Shape):
    def draw_rectangle(self):
        pass

    def draw_circle(self):
        pass


"""
To make Shape conform to the ISP principle, we segregate the actions into different classes
Classes Circle and Rectangle can inherit from class Shape and implement their own draw behaviour

"""


class Shape:
    def draw(self):
        raise NotImplementedError


class Rectangle(Shape):
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        pass
