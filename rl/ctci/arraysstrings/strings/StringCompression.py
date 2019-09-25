class StringCompression:

    def solution_with_dict(self, s):

        char_freq = dict()

        for ch in s:
            if ch in char_freq.keys():
                char_freq.update({ch: char_freq.get(ch) + 1})
            else:
                char_freq.update({ch:1})
        ret_str_list = list()
        for key in char_freq.keys():
            ret_str_list.append(key)
            ret_str_list.append(str(char_freq.get(key)))

        if len(ret_str_list) < len(s):
            ret_str = ''.join(ret_str_list)
            return ret_str
        else:
            return s

print(StringCompression().solution_with_dict('aabbbbbcccd'))
print(StringCompression().solution_with_dict('abc'))