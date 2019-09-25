import unittest

from rl.ctci.arraysstrings.strings.IsUnique import IsUnique


class IsUniqueTests(unittest.TestCase):

    def test_is_unique(self):
        test_obj = IsUnique()

        self.assertTrue(test_obj.is_unique_with_dict('abc'))

    def test_is_unique_empty(self):
        test_obj = IsUnique()

        self.assertTrue(test_obj.is_unique_with_dict(''))