"""
Leetcode Challange: Roman To Integer
Solved by: tonaco.braulio@gmail.com
Date: 09/06/2019


Roman numerals are represented by seven different symbols:

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, 
just two one's added together. Twelve is written as, XII, which is simply X + II. 
The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four 
is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. 
Input is guaranteed to be within the range from 1 to 3999.
"""

# table is a dictionary representing roman character (keys)
# and their respective integer representations
table = {
    "I": 1,
    "IV": 4,
    "V":  5,
    "IX": 9,
    "X":  10,
    "XL": 40,
    "L":  50,
    "XC": 90,
    "C":  100,
    "CD": 400,
    "D":  500,
    "CM": 900,
    "M":  1000
}

class RomanToInteger:
    def __init__(self, symbol):
        self.roman = symbol
        self.integer = self.__getInteger()

    # __getInteger will iterate over each roman character and
    # return its integer value.
    def __getInteger(self):
        intValue = 0
        idx = 0
        while idx < len(self.roman):
            curr = self.roman[idx]
            next = self.__getNext(idx + 1)
        
            # Handle Edge Cases      
            if next is not None and (curr + next) in table.keys():
                intValue += table[curr + next]
                idx += 1
            else:
                intValue += table[curr]
            
            idx += 1
        
        return intValue

    # __getNext will check if the current "idx" position in 
    #  the roman string is within the string bound. 
    def __getNext(self, idx):
        return  self.roman[idx+1] if idx < len(self.roman) - 1 else None