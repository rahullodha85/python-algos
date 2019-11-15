class IsPalindromePermutation:

    def is_permutation_using_dict(self, input):

        temp = dict()

        for ch in input:
            if str(ch).isalnum():
                if ch in temp.keys():
                    temp.update({ch: temp.get(ch) + 1})
                else:
                    temp.update({ch: 1})
        found_odd = False
        for key in temp.keys():
            if temp.get(key) % 2 == 1:
                if found_odd:
                    return False
                found_odd = True

        return True

print(IsPalindromePermutation().is_permutation_using_dict('taco cat'))