# 20221025 - Python OOP - First Steps in OOP
# 01 - Shop - judge: https://judge.softuni.org/Contests/Compete/Index/1935#0


# --------------------- version 1 ------------------------ judge: 100%


class Shop:
    def __init__(self, name: str, items: list):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())
