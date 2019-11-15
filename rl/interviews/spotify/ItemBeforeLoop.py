import collections


class Node:
    def __init__(self, data):
        if data:
            self.data = data
            self.next = None


class ItemBeforeLoop:

    def Solution(self, head: Node) -> Node:

        node_freq = collections.OrderedDict()

        current = head
        loop = False
        while current and not loop:
            if current in node_freq.keys():
                node_freq.update({current: node_freq.get(current) + 1})
                loop = True
                previous_node = None
                for index in range(0, len(node_freq.keys())):
                    if index == 0:
                        if node_freq.get(list(node_freq.keys())[index]) > 1:
                            return None
                    else:
                        previous_node = list(node_freq.keys())[index - 1]
                        if node_freq.get(list(node_freq.keys())[index]) > 1:
                            return previous_node
            else:
                node_freq.update({current: 1})
            current = current.next
        return None
        # if loop:
        #
        # else:
        #     return None


test = Node(1)
test.next = Node(2)
test.next.next = Node(3)
test.next.next.next = Node(4)
test.next.next.next.next = test.next

print(ItemBeforeLoop().Solution(test))