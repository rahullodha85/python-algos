class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TreeTwoSum:

    def findTarget(self, root: TreeNode, k: int) -> bool:
        s = set()
        return self.__findTarget(root, k, s)

    def __findTarget(self, root, k, s) -> bool:
        if not root:
            return False
        test = k - root.val
        if test in s:
            return True
        s.add(root.val)
        return self.__findTarget(root.left, k, s) or self.__findTarget(root.right, k, s)