class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self, data=None):
        if data:
            self.root = TreeNode(data)
        else:
            self.root = None

    def is_empty(self) -> bool:
        return self.root is None

    def search(self, data) -> TreeNode:
        return self.__search(self.root, data=data)

    def __search(self, node: TreeNode, data) -> TreeNode:
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self.__search(node.left, data)
        else:
            return self.__search(node.right, data)


