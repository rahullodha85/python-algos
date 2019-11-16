class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SortedArraytoBST:

    def solution(self, nums):
        return self.to_bst(nums, 0, len(nums))

    def to_bst(self, nums, low, high):
        if low == high:
            return None

        mid = (low + high)//2
        node = TreeNode(nums[mid])
        node.left = self.to_bst(nums, low, mid)
        node.right = self.to_bst(nums, mid+1, high)
        return node