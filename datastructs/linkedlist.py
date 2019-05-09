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

        if curr_node.data == data:
            self.head = curr_node.next
            return
        prev_node = self.head
        curr_node = curr_node.next
        while curr_node is not None:
            if curr_node.data == data:
                prev_node.next = curr_node.next
                return
            curr_node = curr_node.next
            prev_node = prev_node.next

    def contains(self, data) -> bool:
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == data:
                return True
            curr_node = curr_node.next
        return False

    def delete_all(self, data):
        while self.contains(data):
            self.delete_node(data)
