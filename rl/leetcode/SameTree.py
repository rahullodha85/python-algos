from rl.leetcode import TreeNode


class SameTree:

    def solution(self,p: TreeNode, q: TreeNode):
        if not p and not q:
            return True
        if (p and not q) or (q and not p):
            return False
        return p.val == q.val and self.solution(p.left, q.left) and self.solution(p.right, q.right)
