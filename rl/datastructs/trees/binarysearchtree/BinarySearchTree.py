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

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self.__insert(self.root, data)

    def __insert(self, node: TreeNode, data):
        if data == node.data:
            return
        else:
            if data < node.data:
                if node.left is None:
                    node.left = TreeNode(data)
                else:
                    self.__insert(node.left, data)
            else:
                if node.right is None:
                    node.right = TreeNode(data)
                else:
                    self.__insert(node.right, data)
