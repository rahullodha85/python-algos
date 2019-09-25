from rl.ctci.linkedlist.Node import Node


class RemoveDuplicates:

    def solution_with_extra_space(self, head: Node) -> Node:

        curr_node = head

        deduped_data = list()
        while curr_node:
            if curr_node.data not in deduped_data:
                deduped_data.append(curr_node.data)
            curr_node = curr_node.next
        dummy = Node(-1)
        curr_node = dummy
        for data in deduped_data:
            curr_node.next = Node(data)
            curr_node = curr_node.next
        return dummy.next

test = Node(1)
test.add(1)
test.add(2)
test.print_all()
test = RemoveDuplicates().solution_with_set(test)
test.print_all()

test = Node(2)
test.add(2)
test.add(1)
test.print_all()
test = RemoveDuplicates().solution_with_set(test)
test.print_all()