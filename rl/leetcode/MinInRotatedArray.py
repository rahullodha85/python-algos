class MinInRotatedArray:

    def brute_force(self, nums)-> int:

        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                return nums[i]
        return nums[0]

    def binary_search(self, nums) -> int:

        if len(nums) == 0:
            return nums[0]

        left = 0
        right = len(nums) - 1

        if nums[right] > nums[0]:    # no rotation
            return nums[0]

        while left < right:
            mid = left + (right-left)//2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
print(MinInRotatedArray().brute_force([4,1,2,3]))
print(MinInRotatedArray().binary_search([3,4,1,2]))