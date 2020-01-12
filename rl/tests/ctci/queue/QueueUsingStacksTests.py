from rl.ctci.queue.QueueUsingStacks import QueueUsingStacks
import unittest

class QueueUsingStacksTests(unittest.TestCase):

    def setUp(self):
        self.test_obj = QueueUsingStacks()

    def test_peek(self):
        self.test_obj.add(1)
        self.assertEqual(1, self.test_obj.peek())