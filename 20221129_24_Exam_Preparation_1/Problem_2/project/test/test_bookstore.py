from unittest import TestCase, main
from project.bookstore import Bookstore


class TestBookstore(TestCase):
    def setUp(self):
        self.store = Bookstore(15)
        self.books = {
            'Python': 10,
            'Go': 3
        }

    def test_1_correct_init(self):                                                                  # 1        (of 15) : 6%
        self.assertEqual(15, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store.total_sold_books)

    def test_2_books_limit_invalid_book_limit_equal_0(self):                                        # 2, 3     (of 15) : 20%
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = 0
        self.assertEqual('Books limit of 0 is not valid', str(ve.exception))

    def test_3__len__correct_len(self):                                                             # 4        (of 15) : 26%
        self.store.availability_in_store_by_book_titles = self.books
        self.assertEqual(13, len(self.store))

    def test_4_receive_book_no_space_in_store_raise_exception(self):                                # 5        (of 15) : 33%
        self.store.availability_in_store_by_book_titles = self.books
        with self.assertRaises(Exception) as ex:
            self.store.receive_book('Python Advance', 3)
        self.assertEqual('Books limit is reached. Cannot receive more books!', str(ex.exception))

    def test_5_receive_book_new_title_valid_entry_return_number_books(self):                        # 6        (of 15) : 40%
        result = self.store.receive_book('Python Advanced', 2)
        self.assertEqual('2 copies of Python Advanced are available in the bookstore.', result)
        self.assertEqual({'Python Advanced': 2}, self.store.availability_in_store_by_book_titles)

    def test_6_receive_book_existing_title_valid_entry_return_number_books(self):                   # 7        (of 15) : 46%
        self.store.availability_in_store_by_book_titles = self.books
        result = self.store.receive_book('Go', 1)
        self.assertEqual('4 copies of Go are available in the bookstore.', result)

    def test_7_sell_book_no_such_title_in_store_raise_exception(self):                              # 8, 9     (of 15) : 60%
        with self.assertRaises(Exception) as ex:
            self.store.sell_book('Python Advanced', 2)
        self.assertEqual(f"Book Python Advanced doesn't exist!", str(ex.exception))

    def test_8_sell_book_not_enough_copies_of_the_title_raise_exception(self):                      # x, 11    (of 15) : 66%
        self.store.availability_in_store_by_book_titles = self.books
        with self.assertRaises(Exception) as ex:
            self.store.sell_book('Python', 11)
        self.assertEqual(f"Python has not enough copies to sell. Left: 10", str(ex.exception))

    def test_9_sell_book_success(self):                                                       # 10, 12, 13, 14 (of 15) : 93%
        self.store.availability_in_store_by_book_titles = self.books
        result = self.store.sell_book('Go', 3)
        self.assertEqual(f"Sold 3 copies of Go", result)
        self.assertEqual(3, self.store.total_sold_books)
        self.assertEqual({
            'Python': 10,
            'Go': 0
        }, self.store.availability_in_store_by_book_titles)

    def test_10_str_correct(self):                                                                 # 15        (of 15) : 100%
        self.store.availability_in_store_by_book_titles = self.books
        self.assertEqual(
            "Total sold books: 0\n"
            "Current availability: 13\n"
            " - Python: 10 copies\n"
            " - Go: 3 copies",
            str(self.store))


if __name__ == '__main__':
    main()
