import unittest

from day12 import day12


class Day12Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(day12.calculate_total_of_all_numbers("{\"a\":2,\"b\":4}"), 6)
        self.assertEqual(day12.calculate_total_of_all_numbers("[-1,{\"a\":1}]"), 0)

    def test_part_two(self):
        self.assertEqual(day12.calculate_total_of_all_numbers_discounting_red("[1,{\"c\":\"red\",\"b\":2},3]"), 4)
        self.assertEqual(day12.calculate_total_of_all_numbers_discounting_red("[1,\"red\",5]"), 6)


if __name__ == '__main__':
    unittest.main()
