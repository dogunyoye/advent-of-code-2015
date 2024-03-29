import os
import unittest

from day08 import day08


class Day08Test(unittest.TestCase):
    DATA = open(os.path.join(os.path.dirname(__file__), 'resources\\test_input_day08.txt')).read()

    def test_part_one(self):
        self.assertEqual(day08.find_difference(self.DATA), 12)

    def test_part_two(self):
        self.assertEqual(day08.find_difference_new_rules(self.DATA), 19)


if __name__ == '__main__':
    unittest.main()
