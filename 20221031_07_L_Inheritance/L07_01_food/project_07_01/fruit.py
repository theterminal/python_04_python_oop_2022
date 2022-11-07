from project_07_01.food import Food


class Fruit(Food):
    def __init__(self, name: str, expiration_date: str):
        super(Fruit, self).__init__(expiration_date)
        # super().__init__(expiration_date)                 # also works
        self.name = name
