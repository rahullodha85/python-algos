class IsPermutation:
    def is_permutation_sorting(self, s1: str, s2: str)-> bool:

        s1 = list(s1)
        s2 = list(s2)
        s1.sort()
        s2.sort()
        return s1 == s2

