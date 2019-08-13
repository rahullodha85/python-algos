import unittest

from rl.datastructs.stack.StackUsage import StackUsage


class StackUsageTests(unittest.TestCase):

    def test_balance_empty_string(self):
        self.assertTrue(StackUsage().balanced_parentheses(data=''))

    def test_balance_none(self):
        self.assertTrue(StackUsage().balanced_parentheses(data=None))

    def test_balance1(self):
        self.assertTrue(StackUsage().balanced_parentheses(data='[{()}]'))

    def test_balance2(self):
        self.assertTrue(StackUsage().balanced_parentheses(data='[]{}()'))

    def test_balance_not_balanced1(self):
        self.assertFalse(StackUsage().balanced_parentheses(data=')('))

    def test_balance_not_balanced2(self):
        self.assertFalse(StackUsage().balanced_parentheses(data='(]'))
