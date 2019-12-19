from rl.datastructs.trees.binarysearchtree.BinarySearchTree import TreeNode


class SortedArrayToBst:

    def solution(self, nums):
        if len(nums) > 0:
            mid = len(nums)//2

            root = TreeNode(nums[mid])

            root.left = self.solution(nums[:mid])
            root.right = self.solution(nums[mid+1:])

            return root

    def in_order(self, node: TreeNode):
        if not node:
            return
        self.in_order(node.left)
        print(node.data)
        self.in_order(node.right)
test = SortedArrayToBst()
test.in_order(test.solution([1,2,3,4,5,6,7]))
test.in_order(test.solution2([1,2,3]))