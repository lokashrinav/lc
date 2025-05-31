class Solution:
    def confusingNumber(self, n: int) -> bool:
        
        invalid = ['2', '3', '4', '5', '7']

        for elem in invalid:
            if elem in str(n):
                return False
        
        s = str(n)

        hmap = {'6': '9', '9': '6'}

        s2 = ""
        
        for elem in s:
            if elem in hmap:
                s2 += hmap[elem]
            else:
                s2 += elem
        
        s2 = s2[::-1]
        
        if s2 == s:
            return False

        return True

        
