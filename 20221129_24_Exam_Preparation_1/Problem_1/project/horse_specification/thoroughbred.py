from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        # ______________ block 1 _______________ use block 1 or block 2 ________________
        self.speed = min(self.speed + 3, Thoroughbred.MAX_SPEED)

        # ______________ block 2 _______________ use block 1 or block 2 ________________
        # if self.speed + 3 > Thoroughbred.MAX_SPEED:
        #     self.speed = Thoroughbred.MAX_SPEED
        # else:
        #     self.speed += 3
