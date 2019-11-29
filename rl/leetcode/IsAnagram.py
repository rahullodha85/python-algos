class IsAnagram:

    def solution(self, s, t)->bool:

        if len(s) != len(t):
            return False

        NO_OF_CHARS = 256
        count1 = [0] * NO_OF_CHARS
        count2 = [0] * NO_OF_CHARS

        for i in s:
            count1[ord(i)] += 1
        for i in t:
            count2[ord(i)] += 1

        for i in range(0, NO_OF_CHARS):
            if count1[i] != count2[i]:
                return False
        return True


print(IsAnagram().solution('aa','bb'))