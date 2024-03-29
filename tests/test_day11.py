import unittest

from day11 import day11


class Day11Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(day11.find_next_password("abcdefgh"), "abcdffaa")
        self.assertEqual(day11.find_next_password("ghijklmn"), "ghjaabcc")


if __name__ == '__main__':
    unittest.main()
