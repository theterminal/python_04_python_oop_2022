from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            # if product_name == str(product):        # this works too
            if product_name == product.name:
                return product

    def remove(self, product_name: str):
        product = self.find(product_name)

        if product:
            self.products.remove(product)

    def __repr__(self):
        return '\n'.join([f'{x}: {x.quantity}' for x in self.products])
        # return '\n'.join([f'{x.name}: {x.quantity}' for x in self.products])
