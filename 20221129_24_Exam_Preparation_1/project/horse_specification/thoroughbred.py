from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        self.speed = min(self.speed + 3, Thoroughbred.MAX_SPEED)
        # if self.speed + 3 > Thoroughbred.MAX_SPEED:
        #     self.speed = Thoroughbred.MAX_SPEED
        # else:
        #     self.speed += 3
