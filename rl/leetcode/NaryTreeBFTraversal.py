class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:

    def levelOrder(self, root):
        ret_list = []
        if not root:
            return ret_list
        current = [root]
        while current:
            temp = []
            next = []
            for node in current:
                temp.append(node.val)
                next.extend(node.children)
            ret_list.append(temp)
            current = next
        return ret_list
