class MaximumSubarray:

    def brute_force(self, nums) -> int:
        max_sum = -2147483647
        max_count = 0
        sum = 0
        for i in range(0, len(nums)):
            if sum < 0:
                sum = nums[i]
            else:
                sum += nums[i]
            if sum > max_sum:
                max_sum = sum

        return max_sum