class ClimbingStairs:

    def dynamic_programming(self, n: int) -> int:

        if n==1:
            return 1
        stairs = [0]

        stairs.append(1)
        stairs.append(2)

        for index in range(3, n+1):
            stairs.append(stairs[index-1] + stairs[index-2])

        return stairs[n]





