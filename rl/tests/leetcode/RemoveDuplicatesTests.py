import unittest

from rl.leetcode.RemoveDuplicates import ListNode, RemoveDuplicates


class RemoveDuplicatesTests(unittest.TestCase):

    def test1(self):
        data = ListNode(1)
        data.next = ListNode(1)
        data.next.next = ListNode(2)
        testobj = RemoveDuplicates()
        testobj.print_all(data)
        testobj.remove(data)
        testobj.print_all(data)
