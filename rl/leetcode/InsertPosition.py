class InsertPosition:

    def brute_force(self, nums, target: int) -> int:
        for num in nums:
            if num == target:
                return nums.index(num)
            else:
                if num > target:
                    return nums.index(num)
        return nums.__len__()

