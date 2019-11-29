from rl.ctci.linkedlist.Node import Node


class GetMiddle:

    def solution(self, head: Node):

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow.data

test = Node(1)
test.add(2)
test.add(3)
test.add(4)
test.add(5)

print(GetMiddle().solution(test))
test.add(6)
print(GetMiddle().solution(test))
