import unittest

from rl.leetcode.LengthOfLastWord import LengthOfLastWord


class LengthOfLastWordTests(unittest.TestCase):

    def test_brute_force(self):
        test_obj = LengthOfLastWord()
        self.assertEqual(5, test_obj.brute_force(s='Hello World'))

    def test_brute_force_empty_string(self):
        test_obj = LengthOfLastWord()
        self.assertEqual(0, test_obj.brute_force(s=''))

    def test_brute_force_space(self):
        test_obj = LengthOfLastWord()
        print(test_obj.brute_force(s=' '))

    def test_brute_force_single_char(self):
        test_obj = LengthOfLastWord()
        print(test_obj.brute_force(s='a'))
