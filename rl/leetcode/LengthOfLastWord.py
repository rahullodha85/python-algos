class LengthOfLastWord:
    def brute_force(self, s):
        if s.__len__() < 1:
            return 0
        else:
            str_list = s.split()

            if str_list.__len__() > 0:
                test = str_list[str_list.__len__() - 1]
                return test.__len__()
            else:
                return 0
