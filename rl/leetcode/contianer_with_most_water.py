class ContainerWithMostWater:

    def brute_force(self, height) -> int:
        max_area = 0
        for index1 in range(height.__len__()):
            for index2 in range(index1 + 1, height.__len__(), 1):
                max_area = max(max_area, min(height[index1], height[index2]) * (index2 - index1))

        return max_area

    def two_pointer(self, height):
        left = 0
        right = height.__len__() - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

