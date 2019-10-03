from rl.leetcode import TreeNode


class InvertBinaryTree:

    def invertTree(self, root: TreeNode):
        self.__invert_tree(root)
        return root

    def __invert_tree(self, root: TreeNode):
        if root:
            temp = root.left
            root.left = root.right
            root.right = temp
        self.__invert_tree(root.left)
        self.__invert_tree(root.right)