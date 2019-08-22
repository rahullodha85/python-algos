import unittest

from rl.leetcode.InsertPosition import InsertPosition


class InsertPositionTests(unittest.TestCase):

    def test_brute_force_num_exists(self):
        test_obj = InsertPosition()
        output = test_obj.brute_force([1,3,5,7], 5)
        self.assertEqual(2, output)

    def test_brute_force(self):
        test_obj = InsertPosition()
        output = test_obj.brute_force([1,3,5,7], 2)
        self.assertEqual(1, output)

    def test_brute_force_end_insert(self):
        test_obj = InsertPosition()
        output = test_obj.brute_force([1, 3, 5, 7], 8)
        self.assertEqual(4, output)
