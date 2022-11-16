# 20221107 - Python - Python OOP
# 02 - Shop - judge url: https://judge.softuni.org/Contests/Practice/Index/2430#1


class Shop:
    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}                                 # {name: quantity}

    @classmethod
    def small_shop(cls, name: str, type: str):
        return cls(name, type, 10)

    def add_item(self, item_name: str):
        current_capacity = sum(self.items.values())

        if current_capacity == self.capacity:
            return 'Not enough capacity in the shop'

        if item_name in self.items:
            self.items[item_name] += 1
        else:
            self.items[item_name] = 1
            return f'{item_name} added to the shop'

    def remove_item(self, item_name: str, amount: int):
        # __________ block 1 ____________ use block 1 or block 2 ___________
        if item_name not in self.items or amount > self.items[item_name]:
            return f'Cannot remove {amount} {item_name}'

        self.items[item_name] -= amount
        if self.items[item_name] == 0:
            self.items.pop(item_name)
        return f'{amount} {item_name} removed from the shop'

        # __________ block 2 ____________ use block 1 or block 2 ___________
        # if item_name in self.items:
        #     if self.items[item_name] >= amount:
        #         self.items[item_name] -= amount
        #
        #         if self.items[item_name] == 0:
        #             self.items.pop(item_name)
        #
        #         return f'{amount} {item_name} removed from the shop'
        #     else:
        #         return f'Cannot remove {amount} {item_name}'
        # else:
        #     return f'Cannot remove {amount} {item_name}'

    def __repr__(self):
        return f'{self.name} of type {self.type} with capacity {self.capacity}'


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)
