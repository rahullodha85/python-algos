class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0
        for index in range(len(s)):
            if index < len(s) - 1:
                if vals.get(s[index]) < vals.get(s[index + 1]):
                    sum = sum + vals.get(s[index]) * (-1)
                else:
                    sum = sum + vals.get(s[index])
            else:
                sum = sum + vals.get(s[index])
        return sum
