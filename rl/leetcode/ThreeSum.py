class ThreeSum:

    def brute_force(self, nums: [int]) -> [[int]]:
        output = []

        for i in range(nums.__len__()-2):
            for j in range(i+1, nums.__len__()-1):
                for k in range(j+1, nums.__len__()):
                    if nums[i]+nums[j]+nums[k] == 0:
                        output.append([nums[i], nums[j], nums[k]])
        return output

    def optimum(self, nums: [int]) -> [[int]]:
        output = []
        for i in range(nums.__len__()-1):

            s = set()
            temp_sum = 0 - nums[i]
            for j in range(i+1, nums.__len__()):
                temp = temp_sum - nums[j]
                if temp in s:
                    output.append([nums[i], nums[j], temp])
                    break
                s.add(nums[j])

        return output