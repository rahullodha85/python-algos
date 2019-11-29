import unittest

from rl.leetcode.ThreeSum import ThreeSum


class ThreeSumTests(unittest.TestCase):

    def test_brute_force(self):
        three_sum = ThreeSum()
        print(three_sum.brute_force([-1, 0, 1, 2, -1, -4]))

    def test_optimum(self):
        three_sum = ThreeSum()
        print(three_sum.optimum([-1, 0, 1, 2, -1, -4]))