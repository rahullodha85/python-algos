class LongestCommonPrefix(object):
    def brute_force(self, strs: [str]):
        common_prefix = ''
        if strs.__len__() == 1:
            return strs[0]
        if strs.__len__() == 0:
            return ''
        for index1 in range(1, strs.__len__(), 1):
            str1 = strs[index1 - 1]
            str2 = strs[index1]
            if str1 == '' or str2 == '':
                return ''
            short = min(strs[index1].__len__(), strs[index1 - 1].__len__())
            for index2 in range(short):
                if index2 < common_prefix.__len__():
                    if str2[index2] != common_prefix[index2]:
                        common_prefix = common_prefix[0:index2]
                        break
                else:
                    if str1[index2] == str2[index2]:
                        common_prefix = common_prefix + str1[index2]
                    else:
                        break

        return common_prefix
