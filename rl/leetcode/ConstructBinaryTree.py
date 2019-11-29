class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ConstructBinaryTree:

    def pre_order_traverse(self, t: TreeNode):

        if not t:
            return ''
        if not t.left and not t.right:
            return str(t.val) + ''
        if t.right is None:
            return str(t.val) + '(' + self.pre_order_traverse(t.left) + ')'
        return str(t.val) + '(' + self.pre_order_traverse(t.left) + ')' + '(' + self.pre_order_traverse(t.right) + ')'
