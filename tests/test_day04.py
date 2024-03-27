import unittest

from day04 import day04


class Day04Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(day04.find_number_for_hash_starting_with_five_zeroes("abcdef"), 609043)


if __name__ == '__main__':
    unittest.main()
