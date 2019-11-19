class GroupAnagrams:

    def solution_by_sorting(self, strs):

        anagram_dict = dict()
        for val in strs:
            temp = self.get_sorted_anagram(val)
            if temp in anagram_dict.keys():
                anagram_list = anagram_dict.get(temp)
                anagram_list.append(val)
                anagram_dict.update({temp : anagram_list})
            else:
                anagram_list = []
                anagram_list.append(val)
                anagram_dict.update({temp: anagram_list})

        return_list = []
        for key in anagram_dict:
            return_list.append(anagram_dict.get(key))

        return return_list

    def get_sorted_anagram(self, val) -> str:
        list_str = list(val)
        list_str.sort()
        return ''.join(list_str)


print(GroupAnagrams().solution_by_sorting(["eat", "tea", "tan", "ate", "nat", "bat"]))