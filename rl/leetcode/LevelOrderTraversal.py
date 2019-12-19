# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def level_order(self, root):
        return_list = []
        if not root:
            return return_list

        current = [root]
        while current:
            temp = []
            next = []
            for node in current:
                temp.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            return_list.append(temp)
            current = next
        return return_list


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().level_order(root))