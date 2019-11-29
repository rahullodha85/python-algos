from rl.leetcode import TreeNode


class TreeDepth:
    def maxDepth(self, root: TreeNode) -> int:
        return self.get_depth(root)

    def get_depth(self, root: TreeNode)-> int:
        if not root:
            return 0
        return max(self.get_depth(root.left) + 1, self.get_depth(root.right) + 1)