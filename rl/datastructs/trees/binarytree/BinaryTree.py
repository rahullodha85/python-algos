class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, data=None):
        if data:
            self.root = TreeNode(data)
        else:
            self.root = None

    def is_empty(self) -> bool:
        return self.root is None


