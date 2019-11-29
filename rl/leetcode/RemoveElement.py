class RemoveElement:

    def solution(self, nums, val) -> int:
        while(nums.__contains__(val)):
            nums.remove(val)

        return nums.__len__()

print(RemoveElement().solution([1,2,2,3,3,4],3))