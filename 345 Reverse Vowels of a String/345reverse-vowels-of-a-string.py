class Solution:
    def reverseVowels(self, s: str) -> str:
        p1, p2 = 0, len(s) - 1
        lis = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        strList = list(s)
        while p1 < p2:
            if s[p1] in lis and s[p2] in lis:
                strList[p1], strList[p2] = strList[p2], strList[p1]
                p1 += 1
                p2 -= 1
            elif s[p1] in lis:
                p2 -= 1
            elif s[p2] in lis:
                p1 += 1
            else:
                p2 -= 1
                p1 += 1
        
        return ''.join(strList)

            
        