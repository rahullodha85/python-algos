class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:

    def __init__(self, data: int = None):
        if data is None:
            self.head = None
        else:
            self.head = Node(data)

    def append(self, data: int):
        curr_node = self.head
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node

    def insert_front(self, data: int):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_all(self):
        curr_node = self.head
        while curr_node is not None:
            print("%d " % curr_node.data)
            curr_node = curr_node.next

    def delete_node(self, data: int):
        curr_node = self.head
        if curr_node is not None:
            if curr_node.data == data:
                self.head = curr_node.next
                return
        else:
            return
        prev_node = self.head
        curr_node = curr_node.next
        while curr_node is not None:
            if curr_node.data == data:
                prev_node.next = curr_node.next
                return
            curr_node = curr_node.next
            prev_node = prev_node.next

    def contains_iterative(self, data) -> bool:
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == data:
                return True
            curr_node = curr_node.next
        return False

    def contains_recursive(self, data) -> bool:
        return self.contains(data, self.head)

    def contains(self, data, node) -> bool:
        if node is None:
            return False
        else:
            if node.data == data:
                return True
            else:
                return False or self.contains(data, node.next)

    def delete_all(self, data):
        while self.contains_iterative(data):
            self.delete_node(data)

    def get_length_recursive(self) -> int:
        curr_node = self.head
        return self.get_length(curr_node)

    def get_length(self, node) -> int:
        if node is None:
            return 0
        else:
            return 1 + self.get_length(node.next)

    def get_length_iterative(self) -> int:
        curr_node = self.head
        count = 0
        while curr_node is not None:
            count += 1
            curr_node = curr_node.next
        return count

    def get_nth_element(self, index)-> int:
        count = 0
        curr_node = self.head
        while curr_node:
            if count == index:
                return curr_node.data
            count += 1
            curr_node = curr_node.next
        assert False
        return 0

    def nth_node_from_end(self, n) -> int:
        first = self.head
        second = self.head
        for index in range(0, n):
            if first:
                first = first.next
            else:
                assert False
                return 0

        while first:
            first = first.next
            second = second.next
        return second.data

    def middle_node(self) -> int:
        slow = self.head
        fast = self.head

        while fast:
            if fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            else:
                fast = fast.next
        return slow.data