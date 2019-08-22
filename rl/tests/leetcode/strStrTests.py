import unittest

from rl.leetcode.strStr import strStr


class strStrTests(unittest.TestCase):

    def test_solution(self):
        test_obj = strStr()
        test_obj.solution(haystack='hello', needle='ll')

    def test_solution_no_haystack(self):
        test_obj = strStr()
        self.assertEqual(-1, test_obj.solution(haystack='hello', needle='abc'))
