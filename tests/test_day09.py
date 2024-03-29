import os
import unittest

from day09 import day09


class Day09Test(unittest.TestCase):
    DATA = open(os.path.join(os.path.dirname(__file__), 'resources\\test_input_day09.txt')).read()

    def test_part_one(self):
        self.assertEqual(day09.find_distance_of_shortest_route(self.DATA), 605)

    def test_part_two(self):
        self.assertEqual(day09.find_distance_of_longest_route(self.DATA), 982)


if __name__ == '__main__':
    unittest.main()
