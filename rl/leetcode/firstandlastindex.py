class Solution:

    def searchRange(self, nums, target: int):
        if target in nums:
            indexes = []

            # get first index
            for i in range(0, len(nums)):
                if nums[i] == target:
                    indexes.append(i)
                    break

            for i in range(len(nums)-1, -1, -1):
                if nums[i] == target:
                    indexes.append(i)
                    break
            return list(indexes)
        else:
            return [-1, -1]



print(Solution().searchRange([5,7,7,8,10], 8))
print(Solution().searchRange([1], 1))