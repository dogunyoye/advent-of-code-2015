import os
import unittest

from day13 import day13


class Day13Test(unittest.TestCase):
    DATA = open(os.path.join(os.path.dirname(__file__), 'resources\\test_input_day13.txt')).read()

    def test_part_one(self):
        self.assertEqual(day13.find_best_total_change_in_happiness(self.DATA), 330)


if __name__ == '__main__':
    unittest.main()
