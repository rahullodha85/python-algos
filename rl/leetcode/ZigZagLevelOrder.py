# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzag_level_order(self, root):
        return_list = []

        if not root:
            return return_list

        current = [root]
        iteration = 0
        while current:
            temp = []
            next = []

            for node in current:
                temp.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            if iteration % 2 != 0:
                temp.reverse()
            current = next
            iteration += 1
            return_list.append(temp)
        return return_list

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().zigzag_level_order(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
print(Solution().zigzag_level_order(root))