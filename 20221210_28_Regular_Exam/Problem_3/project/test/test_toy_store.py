from unittest import TestCase, main
from project.toy_store import ToyStore


class TestToyStore(TestCase):                                                           # 70/100
    def setUp(self):
        self.store = ToyStore()
        self.store.toy_shelf = {'A': 'Car_1', 'B': 'Car_2', 'C': None}

    def test_0_init_correct(self):
        self.assertEqual({'A': 'Car_1', 'B': 'Car_2', 'C': None}, self.store.toy_shelf)

    def test_1_init_correct(self):
        self.store.toy_shelf = {'A': None}
        self.assertEqual({'A': None}, self.store.toy_shelf)

    def test_2_add_toy(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('K', "Car")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_3_add_toy(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('A', 'Car_1')
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_4_add_toy(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('B', 'Car_1')
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_5_add_toy(self):
        self.assertEqual("Toy:Car_3 placed successfully!", self.store.add_toy('C', 'Car_3'))

    def test_6_remove_toy(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('K', "Car")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_7_remove_toy(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('A', "Bimbo")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_8_remove_toy(self):
        self.assertEqual("Remove toy:Car_1 successfully!", self.store.remove_toy('A', "Car_1"))


if __name__ == '__main__':
    main()
