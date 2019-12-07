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

    def delete(self, data):
        return self.__delete(data, self.root)

    def __delete(self, data, root):
        #locate node
        if root is None:
            return
        if data < root.data:
            root.left = self.__delete(data, root.left)
        elif data > root.data:
            root.right = self.__delete(data, root.right)
        #node found
        else:
            #check if node has one child
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            # node has two children
            #locate inorder successor
            temp = self.min_value_node(root.right)
            root.data = temp.data
            root.right = self.__delete(temp.data, root.right)

        return root

    def min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(f'{node.data} ')
            self.in_order_traversal(node.right)


bst = BinarySearchTree(50)
print(f'root node: {bst.root.data}')
print(f'is empty: {bst.is_empty()}')
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)
bst.in_order_traversal(bst.root)
bst.delete(20)
print('after deleting')
bst.in_order_traversal(bst.root)
bst.delete(30)
print('after deleting')
bst.in_order_traversal(bst.root)
bst.delete(50)
print('after deleting')
bst.in_order_traversal(bst.root)
