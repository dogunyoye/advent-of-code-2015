import unittest

from day02 import day02


class Day02Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(day02.calculate_total_square_feet("2x3x4"), 58)

    def test_part_two(self):
        self.assertEqual(day02.calculate_feet_of_ribbon("2x3x4"), 34)


if __name__ == '__main__':
    unittest.main()
