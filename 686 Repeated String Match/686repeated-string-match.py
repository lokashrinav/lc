class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:

        '''
        abcd da
        '''

        if b in a:
            return 1
        
        if b in a + a:
            return 2
        
        ind = b.find(a)

        if ind == -1:
            return -1
        
        if ind != 0 and b[-ind:] != a[:ind]:
            return -1
        
        for i in range(ind, len(b)):
            if a[(i - ind) % len(a)] != b[i]:
                return -1
        
        return ceil((len(b) - ind) / len(a)) + (1 if ind != 0 else 0)
        #print(int(ceil(len(b) - ind) / len(a)) + 1)
        

        

        






        