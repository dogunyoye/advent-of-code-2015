import unittest

from day05 import day05


class Day05Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(day05.find_number_of_nice_strings("ugknbfddgicrmopn"), 1)

    def test_part_two(self):
        self.assertEqual(day05.find_number_of_nice_strings_with_new_rules("qjhvhtzxzqqjkmpb"), 1)


if __name__ == '__main__':
    unittest.main()
