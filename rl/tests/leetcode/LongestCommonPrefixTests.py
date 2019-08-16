import unittest

from rl.leetcode.LongestCommonPrefix import LongestCommonPrefix


class LongestCommonPrefixTests(unittest.TestCase):
    
    def setUp(self):
        self.lcp = LongestCommonPrefix()

    def test_brute_force(self):
        self.assertEqual('fl', self.lcp.brute_force(['flower', 'flow', 'flight']))

    def test_brute_force_2(self):
        self.assertEqual('f', self.lcp.brute_force(['flower', 'flow', 'faaaaaa']))

    def test_brute_force_3(self):
        self.assertEqual('a', self.lcp.brute_force(['acc', 'aab', 'aaaab']))

    def test_brute_force_empty_str(self):
        self.assertEqual('', self.lcp.brute_force(['flower', 'flow', '']))

    def test_brute_force_no_common_prefix(self):
        self.assertEqual('', self.lcp.brute_force(['b', 'ca', 'cab']))

    def test_brute_force_no_common_prefix_2(self):
        self.assertEqual('', self.lcp.brute_force(['ca', 'cab', 'b']))

    def test_brute_force_only_one_str(self):
        self.assertEqual('abc', self.lcp.brute_force(['abc']))

    def test_brute_force_only_empty_list(self):
        self.assertEqual('', self.lcp.brute_force([]))
