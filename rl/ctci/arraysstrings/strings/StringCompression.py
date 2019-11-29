class StringCompression:

    def solution_with_dict(self, s):

        char_freq = dict()
        ret_str_list = list()

        for ch in s:
            if ch in char_freq.keys():
                char_freq.update({ch: char_freq.get(ch) + 1})
            else:
                if len(char_freq.keys()) > 0:
                    for key in char_freq:
                        ret_str_list.append(key)
                        ret_str_list.append(str(char_freq.get(key)))
                    char_freq.clear()
                char_freq.update({ch: 1})

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
print(StringCompression().solution_with_dict('aabbaaccc'))