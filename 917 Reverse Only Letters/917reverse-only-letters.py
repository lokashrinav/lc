class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        res = []

        for elem in s:
            if elem.isalpha():
                res.append(elem)
        
        res = res[::-1]

        s = list(s)
        ind = 0

        for i in range(len(s)):
            if s[i].isalpha():
                s[i] = res[ind]
                ind += 1
        
        return ''.join(s)
