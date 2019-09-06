class TwoSumReturnIndex:

    def two_sum(self, numbers, target):
        output = []
        for index in range(numbers.__len__()):
            diff = target - numbers[index]
            if numbers.__contains__(diff):
                output.append(index + 1)
                numbers[index] = -1
                output.append(numbers.index(diff) + 1)
                return output
