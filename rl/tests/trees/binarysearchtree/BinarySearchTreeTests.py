import unittest

from rl.datastructs.trees.binarysearchtree.BinarySearchTree import BinarySearchTree, TreeNode


class BinarySearchTreeTests(unittest.TestCase):

    def test_init_empty(self):
        tree = BinarySearchTree()
        self.assertIsNone(tree.root)

    def test_init(self):
        tree = BinarySearchTree(2)
        self.assertEqual(2, tree.root.data)
        self.assertIsNone(tree.root.left)
        self.assertIsNone(tree.root.right)

    def test_is_empty_empty_tree(self):
        self.assertTrue(BinarySearchTree().is_empty())

    def test_is_empty_not_empty_tree(self):
        self.assertFalse(BinarySearchTree(2).is_empty())

    def test_search(self):
        tree = BinarySearchTree(5)
        tree.root.left = TreeNode(4)
        tree.root.left.left = TreeNode(3)
        tree.root.right = TreeNode(6)

        self.assertEqual(3, tree.search(3).data)
