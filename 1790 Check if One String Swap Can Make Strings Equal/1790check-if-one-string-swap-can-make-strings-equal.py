class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        ind1 = None
        ind2 = None
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if ind1 is not None and ind2 is not None:
                    return False
                elif ind1 is not None:
                    ind2 = i
                else:
                    ind1 = i

        if ind1 is not None and ind2 is not None:
            return s1[ind1] == s2[ind2] and s1[ind2] == s2[ind1]
        elif ind1 is not None:
            return False
        else:
            return True