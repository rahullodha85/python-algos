class ThreeSum:

    def brute_force(self, nums: [int]) -> [[int]]:
        output = []

        for i in range(nums.__len__()-2):
            for j in range(i+1, nums.__len__()-1):
                for k in range(j+1, nums.__len__()):
                    if nums[i]+nums[j]+nums[k] == 0:
                        output.append([nums[i], nums[j], nums[k]])
        return output

    def optimum(self, nums):
        output = []
        for i in range(len(nums)-1):

            s = set()
            temp_sum = 0 - nums[i]
            for j in range(i+1, len(nums)):
                temp = temp_sum - nums[j]
                if temp in s:
                    list = [nums[i], nums[j], temp]
                    list.sort()
                    if list not in output:
                        output.append(list)
                s.add(nums[j])

        return output

print(ThreeSum().optimum([-1,0,1,2,-1,-4]))