class MaskPersonalInfo:

    def brute_force(self, S: str) -> str:
        if S.__contains__('@'):
            S = S.lower()
            strings = S.split('@')
            temp = strings[0]
            temp = temp[0] + '*****' + temp[temp.__len__()-1]

            return_val = temp + '@' + strings[1]
            return return_val
        else:
            pass