from abc import ABC, abstractmethod


class Duck(ABC):
    @abstractmethod
    def quack(self):
        pass


class Walk(ABC):
    @abstractmethod
    def walk(self):
        pass


class Fly(ABC):
    @abstractmethod
    def fly(self):
        pass


class RubberDuck(Duck):
    def quack(self):
        return "Squeek"


class RobotDuck(Duck, Walk, Fly):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    def quack(self):
        return 'Robotic quacking'

    def walk(self):
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0


robot = RobotDuck()
rubber = RubberDuck()

print(robot.quack())
print(rubber.quack())
