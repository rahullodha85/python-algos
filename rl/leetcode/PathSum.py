class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class PathSum:
    def hasPathSum(self, root: TreeNode, sum):
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)
print(PathSum().hasPathSum(root, 22))