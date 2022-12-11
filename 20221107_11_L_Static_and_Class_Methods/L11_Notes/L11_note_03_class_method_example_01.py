# 20221107 - Python - Python OOP
# Note 03 - Class Methods - Example 01


class Pizza:
    def __init__(self, ingredients: list):
        self.ingredients = ingredients

    @classmethod
    def pepperoni(cls):
        ingredients = ['tomato sauce', 'parmesan', 'pepperoni']
        return cls(ingredients)

    @classmethod
    def margarita(cls, extra_ingredients: list = None):
        ingredients = ['tomato sauce', 'mozzarella']
        if extra_ingredients:
            ingredients.extend(extra_ingredients)
        return cls(ingredients)

    def bake(self):
        return f'baking pizza with {self.ingredients}'


pepperoni = Pizza.pepperoni()
margarita = Pizza.margarita(['extra_ingredient_1', 'extra_added_2'])

print(pepperoni.ingredients)                                    # ['tomato sauce', 'parmesan', 'pepperoni']
print(margarita.ingredients)                                    # ['tomato sauce', 'mozzarella', 'extra_ingredient_1', 'extra_added_2']

print(pepperoni.bake)                                           # <bound method Pizza.bake of <__main__.Pizza object at 0x10fb87220>>
print(margarita.bake)                                           # <bound method Pizza.bake of <__main__.Pizza object at 0x10fb87280>>

print(pepperoni.bake())                                         # baking pizza with ['tomato sauce', 'parmesan', 'pepperoni']
print(margarita.bake())                                         # baking pizza with ['tomato sauce', 'mozzarella', 'extra_ingredient_1', 'extra_added_2']
