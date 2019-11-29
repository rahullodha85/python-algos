import unittest

from rl.leetcode.ClimbingStairs import ClimbingStairs


class ClimbingStairsTests(unittest.TestCase):

    def test_dynamic_programming(self):
        climbing_staris = ClimbingStairs()

        self.assertEqual(8, climbing_staris.dynamic_programming(5))