# 20221124 - Python OOP - Testing


import unittest


"""
File name must start with 'test_' in order to be able to start/test file/test from the terminal!
Every test (test function) must start with 'test_'
"""


class SimpleTest(unittest.TestCase):
    def test_upper_1(self):
        string = 'foo'                                  # arrange
        result = string.upper()                         # act
        expected_result = 'FOO'
        self.assertEqual(expected_result, result)       # assert

    def test_upper_2(self):
        string = 'foo'                                  # arrange
        result = string.upper()                         # act
        expected_result = 'FOOa'
        self.assertEqual(expected_result, result)       # assert


if __name__ == '__main__':
    unittest.main()
