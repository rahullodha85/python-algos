import unittest

from rl.leetcode.MaskPersonalInfo import MaskPersonalInfo


class MaskPersonalInfoTests(unittest.TestCase):

    def test_email(self):
        test_obj = MaskPersonalInfo()
        print(test_obj.brute_force('ababababab@test.com'))