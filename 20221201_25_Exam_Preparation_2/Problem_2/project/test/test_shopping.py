from unittest import TestCase, main
from project.shopping_cart import ShoppingCart


class TestShoppingCart(TestCase):
    def setUp(self):
        self.shop = ShoppingCart('TestShopName', 1000.5)

    def test_1_correct_init(self):                                          # 1, 2, 3   : 23/100
        self.assertEqual('TestShopName', self.shop.shop_name)
        self.assertEqual(1000.5, self.shop.budget)
        self.assertEqual({}, self.shop.products)

    def test_2_shop_name_setter_raise_ve(self):                             # no change in result
        with self.assertRaises(ValueError) as ve:
            self.shop.shop_name = 'Test Shop Name'
        self.assertEqual('Shop must contain only letters and must start with capital letter!', str(ve.exception))

    def test_3_shop_name_setter_name_start_with_num_raise_ve(self):         # no change in result
        with self.assertRaises(ValueError) as ve:
            self.shop.shop_name = '12Shop'
        self.assertEqual('Shop must contain only letters and must start with capital letter!', str(ve.exception))

    def test_4_add_to_cart_invalid_value_raise_ve(self):                    # 4, 5      : 38/100
        with self.assertRaises(ValueError) as ve:
            self.shop.add_to_cart('test_product', 200)
        self.assertEqual("Product test_product cost too much!", str(ve.exception))

    def test_5_add_to_cart_valid_value(self):                               # 6, 7      : 53/100
        self.shop.add_to_cart('test_product_1', 10)
        self.assertEqual('test_product_2 product was successfully added to the cart!', self.shop.add_to_cart('test_product_2', 20))
        self.assertEqual({'test_product_1': 10, 'test_product_2': 20}, self.shop.products)

    def test_6_remove_existing_product_from_cart(self):                     # 8, 9         : 69/100
        self.shop.products = {'product_1': 10, 'product_2': 20}
        self.assertEqual(f"Product product_1 was successfully removed from the cart!", self.shop.remove_from_cart('product_1'))
        self.assertEqual({'product_2': 20}, self.shop.products)

    def test_7_remove_non_existing_product_from_cart_raise_ve(self):        # 10           : 76/100
        self.shop.products = {'product_1': 20}
        with self.assertRaises(ValueError) as ve:
            self.shop.remove_from_cart('non_existing_product')
        self.assertEqual(f'No product with name non_existing_product in the cart!', str(ve.exception))

    def test_8__add__(self):                                                # 11           : 84/100
        first = self.shop
        first.add_to_cart('from_first', 1)
        second = ShoppingCart('SecondTest', 100)
        second.add_to_cart('from_second', 2)
        merged = first.__add__(second)
        self.assertEqual('TestShopNameSecondTest', merged.shop_name)
        self.assertEqual(1100.5, merged.budget)
        self.assertEqual({'from_first': 1, 'from_second': 2}, merged.products)

    def test_9_buy_products_products_over_budget_raise_ve(self):            # 12           : 92/100
        self.shop.products = {'product_1': 100, 'product_2': 2000}
        total_sum = 2100
        with self.assertRaises(ValueError) as ve:
            self.shop.buy_products()
        self.assertEqual(f'Not enough money to buy the products! Over budget with {(total_sum - self.shop.budget):.2f}lv!', str(ve.exception))

    def test_10_buy_products_valid_entries(self):                           # 13           : 100/100
        self.shop.products = {'product_1': 100, 'product_2': 20}
        total_sum = 120
        self.assertEqual(f'Products were successfully bought! Total cost: {total_sum:.2f}lv.', self.shop.buy_products())


if __name__ == '__main__':
    main()
