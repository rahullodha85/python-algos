class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry_over = 0
        ret_node = ListNode(-1) # Temp place holder
        head = ret_node
        while l1 and l2:
            temp_sum = carry_over + l1.val + l2.val
            carry_over = 0

            if temp_sum > 9:
                carry_over = 1
                temp_sum = temp_sum % 10

            sum_node = ListNode(temp_sum)

            ret_node.next = sum_node
            ret_node = ret_node.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            temp_sum = carry_over + l1.val
            carry_over = 0
            if temp_sum > 9:
                carry_over = 1
                temp_sum = temp_sum % 10

            sum_node = ListNode(temp_sum)
            ret_node.next = sum_node
            ret_node = ret_node.next
            l1 = l1.next
        while l2:
            temp_sum = carry_over + l2.val
            carry_over = 0
            if temp_sum > 9:
                carry_over = 1
                temp_sum = temp_sum % 10

            sum_node = ListNode(temp_sum)
            ret_node.next = sum_node
            ret_node = ret_node.next
            l2 = l2.next

        if carry_over != 0:
            sum_node = ListNode(carry_over)
            ret_node.next = sum_node
        return head.next


l1 = ListNode(9)
l1.next = ListNode(1)
l1.next.next = ListNode(6)

l2 = ListNode(0)

test = Solution().addTwoNumbers(l1, l2)
test