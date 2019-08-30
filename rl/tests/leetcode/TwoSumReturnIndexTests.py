import unittest

from rl.leetcode.TwoSumReturnIndex import TwoSumReturnIndex


class TwoSumReturnIndexTests(unittest.TestCase):

    def test_two_sum(self):
        testobj = TwoSumReturnIndex()
        print(testobj.two_sum([1,2,3], 4))
