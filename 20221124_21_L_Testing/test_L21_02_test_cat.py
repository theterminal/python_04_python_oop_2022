# 20221124 - Python - Python OOP - Testing
# 02 - Test Cat - judge url: https://judge.softuni.org/Contests/Practice/Index/1948#1


class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')
        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False


from unittest import TestCase, main


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat('Jerry')

    def test_correct_init(self):    # not in the problem but good for practice
        self.assertEqual('Jerry', self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_increased_cat_size_after_eating(self):                         # test 1:               1, x, x, x, x     20%
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_cat_is_fed_after_eating(self):                                 # test 1, 2:            1, 2, x, x, x     40%
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        # self.assertEqual(True, self.cat.fed)      # this also works
        self.assertTrue(self.cat.sleepy)            # not in the problem but good to test

    def test_cat_cannot_eat_after_fed_error(self):                          # test 1, 2, 3:         1, 2, 3, x, x     60%
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))     # 'ex.exeption' returns object, that is why must be cast as string

    def test_cat_cannot_fall_asleep_if_not_fed_error(self):                 # test 1, 2, 3, 4:      1, 2, 3, 4, x     80%
        self.cat.fed = False                                    # could work without this line - cat.fed == False by default

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_is_not_sleepy_after_sleeping(self):                        # test 1, 2, 3, 4, 5:   1, 2, 3, 4, 5     100%
        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()
