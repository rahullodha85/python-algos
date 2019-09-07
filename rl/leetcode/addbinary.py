class AddBinary:

    def solution(self, a: str, b: str) -> str:
        len_a = a.__len__()
        len_b = b.__len__()
        diff = abs(len_b-len_a)

        def add(long_l, short_l, diff) -> str:
            output = []
            carry_over = 0
            for i in range(len(short_l) - 1, -1, -1):
                temp = int(long_l[i + diff]) + int(short_l[i]) + carry_over
                if temp > 1:
                    if temp % 2 == 0:
                        temp = 0
                    else:
                        temp = 1
                    carry_over = 1
                else:
                    carry_over = 0
                output.insert(0, str(temp))

            for i in range(len(long_l) - len(short_l) - 1, -1, -1):
                temp = int(long_l[i]) + carry_over

                if temp > 1:
                    if temp % 2 == 0:
                        temp = 0
                    else:
                        temp = 1
                    carry_over = 1
                else:
                    carry_over = 0
                output.insert(0, str(temp))

            if carry_over == 1:
                output.insert(0, str(carry_over))

            return ''.join(output)

        if len_a > len_b:
            return add(a, b, diff)
        else:
            return add(b, a, diff)


print(AddBinary().solution('100', '110010'))
