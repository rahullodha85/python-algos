import unittest

from rl.ctci.arraysstrings.IsPermutation import IsPermutation


class IsPermutationTests(unittest.TestCase):

    def setUp(self):
        self.test_obj = IsPermutation()

    def test_true(self):
        self.assertTrue(self.test_obj.is_permutation_sorting('abc', 'baac'))