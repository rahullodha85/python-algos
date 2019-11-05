class StrToInt:

    def myAtoi(self, s: str)-> int:
        s = s.strip()
        negative = False
        if s.startswith('-'):
            negative = True
            s = s.split('-')[1]
        int_val = 0
        for ch in s:
            int_val = int_val*10 + int(ch)
        if negative:
            return int_val*-1
        return int_val

print(StrToInt().myAtoi('-42'))