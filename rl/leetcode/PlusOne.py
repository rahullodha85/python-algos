class PlusOne:

    def solution(self, digits):
        carry_over = 0
        digits = list(digits)
        for index in range(len(digits) - 1, -1, -1):
            if index == len(digits) - 1:
                temp = digits[index] + 1
                if temp > 9:
                    carry_over = temp//10
                    temp = temp%10
                digits[index] = temp
            else:
                if carry_over > 0:
                    temp = digits[index] + carry_over
                    carry_over = 0
                    if temp > 9:
                        carry_over = temp//10
                        temp = temp%10
                    digits[index] = temp
        if carry_over > 0:
            digits.insert(0, 1)
        return digits

print(PlusOne().solution([1,2,3]))
print(PlusOne().solution([8,9,9,9]))