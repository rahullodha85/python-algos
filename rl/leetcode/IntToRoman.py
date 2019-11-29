from collections import OrderedDict


class IntToRoman:
    def intToRoman(self, num) -> str:
        vals = OrderedDict({
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000}
        )
        roman = []

        for index in range(len(vals.keys())-1, -1, -1):
            temp = num // vals.get(list(vals.keys())[index])
            for i in range(0, temp):
                roman.append(list(vals.keys())[index])
            num = num % vals.get(list(vals.keys())[index])
        return ''.join(roman)

print(IntToRoman().intToRoman(4))
print(IntToRoman().intToRoman(58))
print(IntToRoman().intToRoman(1994))