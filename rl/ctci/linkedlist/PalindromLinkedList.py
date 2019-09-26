from rl.datastructs.linkedlist import Node
from rl.datastructs.stack.ArrayStack import Stack


class PalindromeLinkedList:

    def is_palindrome_using_stack(self, l: Node)-> bool:
        s = Stack()
        curr_node = l
        while curr_node:
            s.push(curr_node.data)
            curr_node = curr_node.next

        curr_node = l

        while curr_node:
            temp = s.pop()

            if temp != curr_node.data:
                return False
            curr_node = curr_node.next
        return True

l = Node(1)
l.next = Node(2)
l.next.next = Node(1)

print(PalindromeLinkedList().is_palindrome_using_stack(l))