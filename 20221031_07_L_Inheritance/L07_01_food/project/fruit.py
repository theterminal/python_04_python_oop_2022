from L20221101_08_E_Inheritance.L08_01_person.project import Food


class Fruit(Food):
    def __init__(self, name: str, expiration_date: str):
        super(Fruit, self).__init__(expiration_date)
        # super().__init__(expiration_date)                 # also works
        self.name = name
