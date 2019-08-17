import unittest

from rl.datastructs.trees.binarytree.BinaryTree import TreeNode


class BinaryTreeTests(unittest.TestCase):

    def test_init_empty(self):
        tree_node = TreeNode()
        self.assertIsNone(tree_node.data)
        self.assertIsNone(tree_node.left)
        self.assertIsNone(tree_node.right)

    def test_init(self):
        tree_node = TreeNode(2)
        self.assertEqual(2, tree_node.data)
        self.assertIsNone(tree_node.left)
        self.assertIsNone(tree_node.right)
