class RemoveAnagrams:

    def solution_with_extra_memory(self, s) -> list:
        return_list = []
        check_set = set()
        for index in range(0, len(s)):
            temp = list(s[index])
            temp = ''.join(sorted(temp))
            if temp not in check_set:
                return_list.append(s[index])
                check_set.add(temp)

        return sorted(return_list)


s = ['code', 'anagram', 'aaagmnr', 'doce']

print(RemoveAnagrams().solution_with_extra_memory(s))