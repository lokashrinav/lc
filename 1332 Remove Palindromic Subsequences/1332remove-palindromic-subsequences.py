class Solution:
    def removePalindromeSub(self, s: str) -> int:

        '''

        babababa

        '''

        if s == s[::-1]:
            return 1
        else:
            return 2


        