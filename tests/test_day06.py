import unittest

from day06 import day06


class Day06Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(day06.find_how_many_lights_on("toggle 0,0 through 999,0"), 1000)

    def test_part_two(self):
        self.assertEqual(day06.find_total_brightness_of_all_lights("turn on 0,0 through 0,0"), 1)


if __name__ == '__main__':
    unittest.main()
