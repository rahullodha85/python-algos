class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.test = []

    def isValidBST(self, root: TreeNode):
        self.in_order(root)
        return self.is_sorted(self.test)

    def is_sorted(self, test):
        if len(test) == 0 or len(test) == 1:
            return True
        for i in range(1, len(test)):
            if test[i-1] >= test[i]:
                return False
        return True

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            self.test.append(root.val)
            self.in_order(root.right)

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(Solution().isValidBST(root))

print(Solution().isValidBST(None))

print(Solution().isValidBST(TreeNode(0)))