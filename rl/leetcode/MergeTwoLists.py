class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MergeTwoLists:

    def solution(self, l1, l2):
        output = ListNode(0)
        dummy = output

        while l1 and l2:
            if l1.val == l2.val:
                output.next = ListNode(l1.val)
                output = output.next
                output.next = ListNode(l2.val)
                output = output.next
                l1 = l1.next
                l2 = l2.next
            else:
                if l1.val < l2.val:
                    output.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    output.next = ListNode(l2.val)
                    l2 = l2.next
                output = output.next
        if l1:
            while l1:
                output.next = ListNode(l1.val)
                output = output.next
                l1 = l1.next
        else:
            while l2:
                output.next = ListNode(l2.val)
                output = output.next
                l2 = l2.next
        return dummy.next


l1 = ListNode(-9)
l1.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(7)
(MergeTwoLists().solution(l1, l2))