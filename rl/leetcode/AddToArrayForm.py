class AddToArrayForm:

    def solution(self, A, K):
        carry_over = 0
        k_list = []
        while K > 0:
            k_list.insert(0, K % 10)
            K = K // 10

        if len(A) > len(k_list):
            large_list = A
            small_list = k_list
        else:
            large_list = k_list
            small_list = A
        index2 = len(small_list) - 1
        for index in range(len(large_list) - 1, -1, -1):
            if index2 > -1:
                sum = large_list[index] + small_list[index2] + carry_over
                carry_over = 0
                if sum > 9:
                    carry_over = sum // 10
                    sum = sum % 10
                large_list[index] = sum
                index2 -= 1
            else:
                sum = large_list[index] + carry_over
                carry_over = 0
                if sum > 9:
                    carry_over = sum // 10
                    sum = sum % 10
                large_list[index] = sum
        if carry_over > 0:
            large_list.insert(0, carry_over)
        return large_list

print(AddToArrayForm().solution([1,2,0,0], 34))
print(AddToArrayForm().solution([2,7,4], 181))
print(AddToArrayForm().solution([2,1,5], 806))
print(AddToArrayForm().solution([0], 23))
print(AddToArrayForm().solution([9,9,9,9,9,9,9], 1))