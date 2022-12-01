class Person:
    def __init__(self, first_name, last_name, age, id):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.__id = id

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_info(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old'


import unittest


class PersonTests(unittest.TestCase):                           # that is the name
    def setUp(self):                                            # setUp() is executed before EVERY test case in the class!
        self.person = Person("Luc", "Peterson", 25, "0350")

    def test_correct_id_expected_success(self):
        result = self.person._Person__id                        # test of private attribute
        expected = "0350"
        self.assertEqual(expected, result)

    def test_get_full_name(self):
        result = self.person.get_full_name()
        expected_result = "Luc Peterson"
        self.assertEqual(expected_result, result)

    def test_get_info(self):
        result = self.person.get_info()
        expected_result = "Luc Peterson is 25 years old"
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
