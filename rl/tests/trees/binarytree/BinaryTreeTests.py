import unittest

from rl.datastructs.trees.binarytree.BinaryTree import TreeNode, BinaryTree


class BinaryTreeTests(unittest.TestCase):

    def test_init_empty(self):
        tree = BinaryTree()
        self.assertIsNone(tree.root)

    def test_init(self):
        tree = BinaryTree(2)
        self.assertEqual(2, tree.root.data)
        self.assertIsNone(tree.root.left)
        self.assertIsNone(tree.root.right)

    def test_is_empty_empty_tree(self):
        self.assertTrue(BinaryTree().is_empty())

    def test_is_empty_not_empty_tree(self):
        self.assertFalse(BinaryTree(2).is_empty())
