class FirstBadVersion:

    def solution(self, n):
        left = 1
        right = n

        while left < right:
            middle = left + (right - left) // 2
            if self.isBadVersion(middle):
                right = middle
            else:
                left = middle + 1
        return left

    def isBadVersion(self, version):
        pass
