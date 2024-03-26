import unittest

from day03 import day03


class Day03Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(day03.calculate_houses_visited("^v^v^v^v^v"), 2)

    def test_part_two(self):
        self.assertEqual(day03.calculate_houses_visited_with_robo_santa("^v^v^v^v^v"), 11)


if __name__ == '__main__':
    unittest.main()
