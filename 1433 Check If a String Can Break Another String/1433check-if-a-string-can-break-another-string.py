class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        '''

        abe
        acd

        '''

        s1 = sorted(list(s1))
        s2 = sorted(list(s2))

        flag1 = True
        for i in range(len(s1)):
            if s1[i] < s2[i]:
                flag1 = False
        
        flag2 = True
        for i in range(len(s1)):
            if s1[i] > s2[i]:
                flag2 = False
        
        return flag1 or flag2
        