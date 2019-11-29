from rl.ctci.linkedlist.Node import Node


class ReturnNthFromLast:

    def single_pass(self, head: Node, n):

        first = head
        second = head

        for i in range(0, n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        return second.data

test = Node(1)
test.add(3)
test.add(4)
test.add(6)

print(ReturnNthFromLast().single_pass(test, 2))
