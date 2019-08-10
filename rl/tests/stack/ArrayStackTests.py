import unittest

from rl.datastructs.stack.ArrayStack import Stack


class StackTests(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_create_empty(self):

        self.assertEqual(0, self.stack.get_length())

    def test_stack_push(self):
        self.stack.push(1)

        self.assertEqual(1, self.stack.get_length())

    def test_pop_stacl(self):
        self.stack.push(1)
        data = self.stack.pop()

        self.assertEqual(1, data)

    def test_pop_stack_empty(self):
        data = self.stack.pop()

        self.assertIsNone(data)
