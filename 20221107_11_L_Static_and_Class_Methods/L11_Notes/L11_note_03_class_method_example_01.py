# 20221107 - Python - Python OOP
# Note 03 - Class Methods - Example 01


class Pizza:
    def __init__(self, ingredients: list):
        self.ingredients = ingredients

    @classmethod
    def pepperoni(cls):
        return cls(['tomato sauce', 'parmesan', 'pepperoni'])

    @classmethod
    def margarita(cls, extra_ingredients: list = None):
        ingredients = ['tomato sauce', 'mozzarella']
        if extra_ingredients:
            ingredients.extend(extra_ingredients)
        return cls(ingredients)

    def bake(self):
        return f'baking pizza with {self.ingredients}'


pepperoni = Pizza.pepperoni()
margarita = Pizza.margarita(['one more extra ingredient'])

print(pepperoni.ingredients)
print(margarita.ingredients)

print(pepperoni.bake)
print(margarita.bake)
