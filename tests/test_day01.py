import unittest

from day01 import day01


class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(day01.which_floor(")())())"), -3)

    def test_part_two(self):
        self.assertEqual(day01.which_floor_to_basement("()())"), 5)


if __name__ == '__main__':
    unittest.main()
