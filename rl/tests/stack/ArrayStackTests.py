import unittest

from rl.datastructs.stack.ArrayStack import Stack


class StackTests(unittest.TestCase):

    def test_create_empty(self):
        stack = Stack()
        self.assertEqual(0, stack.get_length())
