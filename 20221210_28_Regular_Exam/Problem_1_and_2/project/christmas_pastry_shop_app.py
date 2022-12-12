from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth


class ChristmasPastryShopApp:                                                                   # (1-11 of 29) 56/150
    def __init__(self):
        self.booths: list = []                                  # all created booths (objects)
        self.delicacies: list = []                              # all created delicacies (objects)
        self.income: float = 0.0                                # total income of the pastry shop

    def add_delicacy(self, type_delicacy: str, name: str, price: float):                        # (12-15 of 29) 77/150
        for delicacy in self.delicacies:
            if delicacy.name == name:
                raise Exception(f'{name} already exists!')

        if type_delicacy not in ['Gingerbread', 'Stolen']:
            raise Exception(f'{type_delicacy} is not on our delicacy menu!')

        delicacy_created = ''
        if type_delicacy == 'Gingerbread':
            delicacy_created = Gingerbread(name, price)
        elif type_delicacy == 'Stolen':
            delicacy_created = Stolen(name, price)

        self.delicacies.append(delicacy_created)
        return f'Added delicacy {name} - {type_delicacy} to the pastry shop.'

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):                     # (16-19 of 29) 98/150
        for booth in self.booths:
            if booth.booth_number == booth_number:
                raise Exception(f'Booth number {booth_number} already exists!')

        if type_booth not in ['Open Booth', 'Private Booth']:
            raise Exception(f'{type_booth} is not a valid booth!')

        booth = ''
        if type_booth == 'Open Booth':
            booth = OpenBooth(booth_number, capacity)
        elif type_booth == 'Private Booth':
            booth = PrivateBooth(booth_number, capacity)

        self.booths.append(booth)
        return f'Added booth number {booth_number} in the pastry shop.'

    def reserve_booth(self, number_of_people: int):                                             # (18-21 of 29) 98/150
        for booth in self.booths:
            if not booth.is_reserved:
                booth.reserve(number_of_people)
                return f'Booth {booth.booth_number} has been reserved for {number_of_people} people.'
        else:
            return f'No available booth for {number_of_people} people!'

    def order_delicacy(self, booth_number: int, delicacy_name: str):                            # (x, 23-25 of 29) 124/150
        for booth in self.booths:
            if booth.booth_number == booth_number:
                break
        else:
            raise Exception(f'Could not find booth {booth_number}!')

        for delicacy in self.delicacies:
            if delicacy.name == delicacy_name:
                break
        else:
            raise Exception(f'No {delicacy_name} in the pastry shop!')

        for booth in self.booths:
            if booth.booth_number == booth_number:
                for delicacy in self.delicacies:
                    if delicacy.name == delicacy_name:
                        booth.delicacy_orders.append(delicacy)

        return f'Booth {booth_number} ordered {delicacy_name}.'

    def leave_booth(self, booth_number: int):                                                   # (x, x, x, 29 of 29) 129/150
        orders = 0
        for booth in self.booths:
            if booth.booth_number == booth_number:
                for k in booth.delicacy_orders:
                    orders += k.price
                orders += booth.price_for_reservation
                self.income += orders
                booth.price_for_reservation = 0
                booth.is_reserved = False
                booth.delicacy_orders = []
                return f'Booth {booth_number}:' \
                       f'Bill: {orders:.2f}lv.'

    def get_income(self):
        return f'Income: {self.income:.2f}lv.'


# shop = ChristmasPastryShopApp()
# print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
# print(shop.delicacies[0].details())
# print(shop.add_booth("Open Booth", 1, 30))
# print(shop.add_booth("Private Booth", 10, 5))
# print(shop.reserve_booth(30))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.leave_booth(1))
# print(shop.reserve_booth(5))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.leave_booth(1))
# print(shop.get_income())
