class Node:

    def __init__(self, data):
        if data:
            self.data = data
            self.next = None

    def add(self, data):
        end = Node(data)
        curr = self

        while curr.next:
            curr = curr.next

        curr.next = end

    def print_all(self):
        curr = self

        while curr:
            print(curr.data)
            curr = curr.next
