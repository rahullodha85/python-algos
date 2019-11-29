import unittest

from rl.leetcode.ConstructBinaryTree import ConstructBinaryTree, TreeNode


class ConstructBinaryTreeTests(unittest.TestCase):

    def test_traversal(self):
        tree_node = TreeNode(1)
        tree_node.left = TreeNode(2)
        tree_node.left.left = TreeNode(4)
        tree_node.right = TreeNode(3)
        test_obj = ConstructBinaryTree()
        print(test_obj.pre_order_traverse(tree_node))