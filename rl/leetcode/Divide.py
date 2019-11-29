class Divide:

    def brute_force(self, dividend, divisor):

        negative = False
        if (dividend < 0)^(divisor < 0):
            negative = True

        dividend = abs(dividend)
        divisor = abs(divisor)
        test_sum = 0
        count = 0
        if divisor > dividend:
            return 0
        if divisor == 1:
            if negative:
                return dividend * -1
            else:
                return dividend
        while test_sum < dividend:
            test_sum += divisor
            count += 1
            if dividend - test_sum < divisor:
                break

        if negative:
            return count * -1
        else:
            return count

print(Divide().brute_force(1,2))