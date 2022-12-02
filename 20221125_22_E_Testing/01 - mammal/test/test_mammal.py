from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal('Jim', 'Human', 'Yeah...')

    def test_1_correct_init(self):
        self.assertEqual('Jim', self.mammal.name)
        self.assertEqual('Human', self.mammal.type)
        self.assertEqual('Yeah...', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_2_make_sount_does_it_return_the_correct_message(self):
        result = self.mammal.make_sound()
        self.assertEqual('Jim makes Yeah...', result)

    def test_3_get_kingdom_returns_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual('animals', result)

    def test_4_info_returns_correct_message(self):
        result = self.mammal.info()
        self.assertEqual('Jim is of type Human', result)


if __name__ == '__main__':
    main()
